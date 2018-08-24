#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simplify AWS DataPipeline Deployments
"""
import sys

import pip
from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

# requirements = pip.req.parse_requirements(
#     'requirements.txt', session=pip.download.PipSession(),
# )

dependencies = ['click', 'boto3', 'pyyaml', 'awscli']

# Only install futures package if using a Python version <= 2.7
# if sys.version_info[0] == 2:
#     pip_requirements = [str(r.req) for r in requirements]
# else:
#     pip_requirements = [str(r.req)
#                         for r in requirements if 'futures' not in str(r.req)]

setup(
    name='aws-piper',
    version='0.1.0',
    description='Simplify AWS DataPipeline Deployments',
    long_description=readme,
    author='Patrick Bamba',
    author_email='pbamba@heetch.com',
    url='https://github.com/heetch/aws-piper',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    # scripts=['scripts/lambda'],
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
