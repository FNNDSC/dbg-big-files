# `dbg-bigfiles`

[![Version](https://img.shields.io/docker/v/fnndsc/dbg-bigfiles?sort=semver)](https://hub.docker.com/r/fnndsc/dbg-bigfiles)
[![MIT License](https://img.shields.io/github/license/fnndsc/dbg-bigfiles)](https://github.com/FNNDSC/dbg-bigfiles/blob/main/LICENSE)
[![Build](https://github.com/FNNDSC/dbg-bigfiles/actions/workflows/build.yml/badge.svg)](https://github.com/FNNDSC/dbg-bigfiles/actions)

`dbg-bigfiles` is a _ChRIS_ _fs_ plugin that creates files
of random data. It is for stress-testing _CUBE_'s capacity to
deal with large amounts of data.

## Example

```bash
singularity exec docker://fnndsc/dbg-bigfiles bigfiles --total '1.8GiB' --size '614.4MiB' output/
```
