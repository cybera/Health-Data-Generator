#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

config = {
    'name': 'Faker',
    'description': 'Fake data generator for python',
    'author': 'Hrishikesh Huilgolkar, Barton Satchwill',
    'author_email': 'hrishikesh911@gmail.com, barton.satchwill@gmail.com',
    'url': '',
    'download_url': '',
    'dependency_links':[''],
    'version': '0.0.1',
    'install_requires': [''],
    'tests_require': ['nose'],
    'packages': ['faker'],
    'scripts': ['']
}

setup(**config)
