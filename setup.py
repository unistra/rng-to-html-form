#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
                        link.startswith('-f')]

setup(
    name='rng-to-html-form',
    version='1.0.1',
    author='di-dip-unistra',
    author_email='di-dip@unistra.fr',
    maintainer='di-dip-unistra',
    maintainer_email='di-dip@unistra.fr',
    url='https://github.com/unistra/rng-to-html-form',
    license='PSF',
    description='Takes an rng file and makes an html form',
    long_description=long_description,
    packages=find_packages(),
    download_url='http://pypi.python.org/pypi/rng-to-html-form',
    install_requires=libraries,
    dependency_links=dependency_links,
    keywords=['lxml', 'python', 'rng', 'xml', 'form', 'html'],
    entry_points={},
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4'
    )
)
