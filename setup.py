from setuptools import setup

setup(
    name             = 'bigfiles',
    version          = '1.0.0',
    description      = 'Create files of random data',
    author           = 'FNNDSC',
    author_email     = 'dev@babyMRI.org',
    url              = 'https://github.com/FNNDSC/dbg-bigfiles',
    py_modules       = ['bigfiles'],
    install_requires = ['chris_plugin', 'tqdm'],
    license          = 'MIT',
    python_requires  = '>=3.10.2',
    entry_points     = {
        'console_scripts': [
            'bigfiles = bigfiles:main'
            ]
        },
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
