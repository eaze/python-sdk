#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shift_planning',
      version='0.1.0',
      description='Shiftplanning API',
      url='https://www.shiftplanning.com/api/',
      packages=find_packages(),
      install_requires = ['simplejson'])
