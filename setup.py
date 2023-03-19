from setuptools import setup, find_packages

setup(
    name='bujango',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'asgiref==3.6.0','sqlparse==0.4.3'
    ],
    author='Tu nombre',
    author_email='andresfelipe200004@gmail.com',
    description='Una biblioteca que contiene solo el ORM de Django'
)