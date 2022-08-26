from setuptools import setup
from setuptools import find_packages

setup(
    name = 'coordinates-analyzer',
    version = '0.0.1',
    description = 'A Python CLI program that mathematically compare 2 different molecular structures (.xyz file), based on their atomic coordinates.',
    long_description = './README.md',
    license = './LICENSE',
    author = 'Matheus Rauen C. da Luz',
    author_email = 'matheus.rauen@grad.ufsc.br',
    url='https://https://github.com/m-rauen',
    packages = find_packages(),
    install_requires = ['Click'],
    entry_points = {
        'console_scripts': [
            'coords-analyze=src.main:Testing',
        ],
    },
)