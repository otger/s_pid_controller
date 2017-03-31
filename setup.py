#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# Read README and CHANGES files for the long description
here = os.path.abspath(os.path.dirname(__file__))
README  = open(os.path.join(here, 'README.md')).read()
PACKAGEFULLNAME = 's_pid_controller'
PACKAGENAME = 's_pico_tc08'
DESCRIPTION = 'Module that implements a PID controller for an entropy system'
LONG_DESCRIPTION = ''
AUTHOR = 'Otger Ballester'
AUTHOR_EMAIL = 'otger@ifae.es'
LICENSE = open(os.path.join(here, 'LICENSE')).read()
URL = None
VERSION = '0.0.2'
RELEASE = 'dev' not in VERSION

print(find_packages('s_pico_tc08'))
# Read the version information
#execfile(os.path.join(here, '__init__.py'))
setup(
      name=PACKAGEFULLNAME,
      version=VERSION,
      description=DESCRIPTION,
      #scripts=scripts,
      requires=['pidcontroller'],
      install_requires=[],
      provides=[PACKAGENAME],
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,
      use_2to3=True,
      classifiers=[
                   "Development Status :: 4 - Beta",
                   "Programming Language :: Python",
                  ],
      #ata=True,
      packages=find_packages()
    #zip_safe=True,
)
