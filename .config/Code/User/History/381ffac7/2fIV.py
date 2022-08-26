from setuptools import setup

setup(
    name = 'coordinates-analyzer',
    version = '0.0.1',
    description = 'A Python CLI program that mathematically compare 2 different molecular structure (.xyz file), based on their atomic coordinates.',
    author = 'Matheus Rauen C. da Luz',
    author_email = 'matheus.rauen@grad.ufsc.br',
    url='https://https://github.com/m-rauen',
    py_modules = ['main'],
    install_requires = ['Click'],
    entry_points = {
        'console_scripts': [
            'coords-analyze = coords-analyze.main:Testing',
        ],
    },
)