from setuptools import setup
from setuptools import find_packages

setup(
    name = 'coordinates-analyzer',
    version = '1.4.0',
    description = 'A Python CLI program that mathematically compare 2 different molecular structures (.xyz file), based on their atomic coordinates.',
    long_description = './README.md',
    license = './LICENSE',
    author = 'Matheus Rauen C. da Luz',
    author_email = 'matheus.rauen@grad.ufsc.br',
    url='https://https://github.com/m-rauen/Coordinates_Analyzer',
    packages = find_packages(),
    install_requires = ['Click',
                        'numpy',
                        'rich',
                        'rich_click'],
    entry_points = {
        'console_scripts': [
            'coords-analyze=cli.main:inputFiles',
        ],
    },
)
