# py-reqres-api-automation

## Introduction

API Automation Framework for reqres.in APIs, built using Python `requests` and `pytest` libraries.

## Installation Instructions
Note: This framework was developed and tested in Mac OS.

* Python 3.9+ - Follow Instructions here to install latest python versions: https://realpython.com/intro-to-pyenv/. Recommended to have a virtualenv created prior to downloading script from Github.
* In the directory of interest, clone the repository:
```
pyenv activate <virtualenv-name> # Skip this step is virtualenv is not created.
git clone https://github.com/hasanibnmansoor/py-reqres-api-automation.git
cd py-reqres-api-automation/
pip install -r requirements.txt
pip install -e .
```
## Framework Structure

This framework follows flat-framework folder structures, and all of the libraries/tests are housed inside `pyreqres` folder.
* Module `api.py` has the helper functions for Requests Operations - GET, POST, PUT, PATCH, DELETE. Methods in this module will be consumed across the `models` package.
* Package `models`: Has modules `login.py`, `register.py` and `users.py` and their related operations.
* Testcases are written in `tests` folder.

## How to Run?
After cloning the package, and installing dependencies, tests can be run using below commands
* (From anywhere in directory) `pytest -v -s --pyargs pyreqres`
* (From Project Root directory) `pytest -v -s`
* If html report is required, `pytest -v -s --html=<report-name>.html --self-contained-html`

## Future Improvements
* Integrate with Circle CI for Automated CI/CD pipeline.
* Customize Reporting

