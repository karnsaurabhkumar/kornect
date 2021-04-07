from setuptools import find_packages, setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kornect',
    packages=find_packages(),
    version='0.1.1',
    description='Set of utilities to rapidly do data analysis',
    author='Saurabh Karn',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
