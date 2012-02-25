import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "GiltAlchemy",
    version = "0.0.1",
    author = "John Quinn",
    author_email = "doofdoof@gmail.com",
    description = ("SQLAlchemy Models for the Gilt API"),
    license = "BSD",
    keywords = "Gilt",
    url = "https://github.com/doofdoofsf/GiltAlchemy",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
