from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent

long_description = open('README.rst').read(),

setup(
    name='bujango',
    version='0.2.6',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    install_requires=[
        'asgiref==3.6.0','sqlparse==0.4.3'
    ],
    platforms=["any"],
    keywords="Django ORM",
    url="https://github.com/Rojas-Andres/bujango",
    author='Andres Rojas',
    author_email='andresfelipe200004@gmail.com',
    description='Una biblioteca que contiene solo el ORM de Django',
    long_description=long_description,
)