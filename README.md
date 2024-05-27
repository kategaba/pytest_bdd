# pytest-bdd-with-selenium

An example showing the usage of pytest-bdd library used with selenium in Python.

## Features

- Write feature files for UI testing with behaviour driven design approach (similar to cucumber)
- Readable and manageable code using Page Object design pattern

## Installation

pytest-bdd-with-selenium requires [Python](https://www.python.org/download) to run.

Use a virtual environment (recommended)

```sh
pip install virtualenv
python3 -m venv pytest-env
source pytest-env/bin/activate
```

Install the dependencies by

```sh
pip install -r requirements.txt
```

## Environment File
All environment related variables are stored in the `.env` file. This file is being ignored by git and you have to create it yourself.

Before you can run tests, you must ensure you have the following in your `.env` file:

```

	PASSWORD = yourPassword

```

## Run the test

Run the Test file

```sh
# filter tests by test module
# note: feature files cannot be run directly
pytest tests/step-defs/test_login.py
```
# References

- pytest-bdd example: https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/
- page object example: https://blog.testproject.io/2019/07/16/develop-page-object-selenium-tests-using-python/