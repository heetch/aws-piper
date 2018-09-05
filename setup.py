#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simplify AWS DataPipeline deployment and management
"""

from setuptools import find_packages
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

dependencies = ['click', 'boto3', 'pyyaml', 'awscli']

setup(
    name='aws-piper',
    version='0.1.1',
    description='Simplify AWS DataPipeline deployment and management',
    long_description=readme,
    author='Patrick Bamba',
    author_email='pbamba@heetch.com',
    url='https://github.com/heetch/aws-piper',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=dependencies,
    platforms='any',
    entry_points={
        'console_scripts': [
            'piper=aws_piper.cli:piper',
        ],
    },
    license='MIT',
    zip_safe=False,
    keywords='aws-piper',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
