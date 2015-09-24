#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

tests_require = [
    'nose',
    'coverage',
]

setup(

    name='groio',
    version='1.0',

    description="A simple library for gro files",
    long_description=readme,

    url='https://github.com/HubLot/groio',

    # Author details
    author='Jonathan Barnoud, Hubert Santuz',
    author_email='jonathan@barnoud.net, hubert.santuz@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],


    packages=find_packages(exclude=['tests*']),

    # List additional groups of dependencies here (tests)
    # To install, use
    # $ pip install -e .[tests]
    extras_require=dict(
        tests=tests_require,
    ),
    tests_require=tests_require,
    test_suite='tests'

)
