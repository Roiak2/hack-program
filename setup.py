#!/usr/bin/env python

"""
Calls 'pip install -e' to install package locally for testing
"""

#import package
from setuptools import setup


#building command
setup(
    name = "confirm_appointment",
    version = "0.0.1",
    author = "Roí A.K.",
    author_email = "ra3040@columbia.edu",
    license = "GPLv3",
    description = "A package for confirming or cancelling doctor's appointments",
    classifiers = ["Programming Language :: Python :: 3"],
    entry_points = {
        "console_scripts": ["confirm_appointment = confirm_appointment.__main__:main"]
    },

)