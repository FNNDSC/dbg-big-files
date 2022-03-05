#!/usr/bin/env python

import sys
import math
import random
from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from chris_plugin import chris_plugin
import tqdm

parser = ArgumentParser(description='Create files of random data',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-s', '--seed', default=None,
                    help='random number generator seed')
parser.add_argument('-t', '--total', type=str, default='5GiB',
                    help='minimum total size of all output (units: B, MiB, GiB)')
parser.add_argument('-z', '--size', type=str, default='2MiB',
                    help='size of individual files (units: B, MiB, GiB)')

CHUNK_SIZE = 1048576


@chris_plugin(
    parser=parser,
    title='Create files of random data',
    category='Debug',
)
def main(options: Namespace, outputdir: Path):

    try:
        seed = int(options.seed)
    except TypeError:
        seed = options.seed

    random.seed(seed)

    final_total: int = units(options.total)
    per_size: int = units(options.size)
    current_total = 0
    n = 0

    with tqdm.tqdm(total=final_total, unit_scale=True, unit='B') as pbar:
        while current_total < final_total:
            output_file = outputdir / f'file-{n}.dat'
            with output_file.open('wb') as f:
                file_size = 0
                while file_size < per_size:
                    next_chunk_size = min(per_size - file_size, CHUNK_SIZE)
                    data = random.randbytes(next_chunk_size)
                    f.write(data)
                    file_size += next_chunk_size
                    pbar.update(next_chunk_size)
            pbar.write(str(output_file))
            n += 1
            current_total += file_size


def units(u: str) -> int:
    num, un = split_units(u)
    if un == 'b':
        return math.ceil(num)
    if un == 'mib':
        return math.ceil(num * 1048576)
    if un == 'gib':
        return math.ceil(num * 1073741824)
    die(f'unrecognized units "{un}" in: {u}')


def split_units(u: str) -> tuple[float, str]:
    split = u.split()
    if len(split) > 2:
        die(f'cannot parse: "{u}"')
    if len(split) == 2:
        return try_parse(split[0], split[1], u)

    for i, c in enumerate(u):
        if c.isdigit() or c == '.':
            continue
        return try_parse(u[:i], u[i:], u)

    return try_parse(u, 'B', u)


def try_parse(n: str, u: str, orig: str) -> tuple[float, str]:
    if not u.endswith('B'):
        u += 'B'
    try:
        return float(n), u.lower()
    except TypeError:
        die(f'cannot parse: "{orig}"')


def die(msg: str) -> None:
    print(msg, file=sys.stderr)
    sys.exit(1)


assert split_units('100 Mi') == (100, 'mib')
assert split_units('100 MiB') == (100, 'mib')
assert split_units('100MiB') == (100, 'mib')
assert split_units('100.MiB') == (100.0, 'mib')
assert split_units('100.1MiB') == (100.1, 'mib')
assert split_units('100.1 MiB') == (100.1, 'mib')


if __name__ == '__main__':
    main()
