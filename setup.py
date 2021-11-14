from distutils.core import setup
from setuptools import find_packages

setup(name='en88ukaz',
version='0.1',
author_email='hamideh.hamidnezhad@fau.de',
packages=find_packages(),
install_requires=['numpy','Pillow','ipywidgets'])

