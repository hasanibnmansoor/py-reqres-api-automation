"""Setup script for py-reqres-api-automation"""

import os.path

from setuptools import find_packages, setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="py-reqres-api-automation",
    version="1.0.0",
    description="Python API Test Automation Framework for ReqRes.in APIs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasanibnmansoor/py-reqres-api-automation",
    author="Hasan Sadhir Mohammed Mansoor",
    author_email="hasanibnmansoor@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "pytest",
        "pytest-sugar",
        "pytest-html",
        "pytest-rerunfailures",
    ],
)
