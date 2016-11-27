try:
  from setuptools import setup, find_packages
except ImportError:
  from distutils.core import setup

setup(
  name       = 'health_data_generator',
  version      = '0.0.1',
  description    = '',
  author       = 'Barton Satchwill',
  author_email   = 'barton.satchwill@cybera.ca',
  url        = '',
  download_url   = '',
  install_requires = [],
  dependency_links = [],
  tests_require  = ['nose'],
  packages     = find_packages(exclude=['docs', 'tests']),
  scripts      = ['scripts/generate']
)

