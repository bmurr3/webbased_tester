# setup.py

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='webbased_tester',
    version='0.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements
)
