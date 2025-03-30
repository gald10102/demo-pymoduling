# setup.py
from setuptools import setup, find_packages

setup(
    name="my_module",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # List dependencies here
    test_suite='tests',  # Automatically find tests
    author="Gal",
    author_email="your.email@example.com",
    description="A simple greeting module",
    long_description="This module provides a simple function to greet a person.",
    long_description_content_type="text/markdown",
    url="https://github.com/gald10102/demo-pymoduling",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
