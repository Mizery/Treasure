#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='Treasure',
      version='1',
      description='Hunt for sensitive information on github.',
      author='GWF',
      author_email='gwf@gwf.ninja',
      url='https://twitter.com/GuerrillaWF',
      packages=find_packages(),
      scripts = ['treasure']
     )
