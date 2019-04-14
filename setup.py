"""
Setup Script
    Describes to `pip` how to install `bazaarci` with abstract dependencies.
    See `requirements.txt` for the concrete dependencies.
"""

from setuptools import setup

setup(
    name='bazaarci',
    version='0.1',
    description='A digraph dependency based runner and CI tool.',
    author='Tom Manner',
    author_email='tom.s.manner@gmail.com',
    url='https://www.github.com/tsmanner/BazaarCI',
    # Packages to install
    packages=[
        'bazaarci',
    ],
)
