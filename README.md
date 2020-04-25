homefinder
==========

Django Web application for 7WCM00033 module

Install Python 3.7+
-------------------

Visit https://www.python.org/downloads/ for instructions on installing python.

Note: the application has been tested on macOS Catalina (10.15.3) with python 3.7.4

Create virtual environment
--------------------------

```bash
$ python3 -m venv env
```

Activate virtual environment
----------------------------

```bash
$ source env/bin/activate
```

Install  mysql
--------------
This is required for deploying to pythonanywhere
```bash
$ brew install mysql
```

Install ChromeDriver (required for web testing)
------------------------------------------------
Ensure Chromium/Google Chrome is installed in a recognized location ChromeDriver expects you to have Chrome installed in the default location for your platform.
Download an appropriate version of ChromeDriver binary depending on the installed version of chrome, see https://sites.google.com/a/chromium.org/chromedriver/downloads
Include the ChromeDriver location in your PATH environment variable

Install python dependencies
---------------------------
```bash
$ pip install -r requirements.txt
```

Local development
-----------------
```bash
$ export DJANGO_DEBUG=True
$ python manage.py migrate
$ python manage.py runserver
```

Execute web tests
-----------------

```bash
$ python -m pytest -k webtest
$ python -m pytest -k cms (to execute cms tests)
$ python -m pytest -k ims (to execute ims tests)
```

Execute unit tests
-----------------

```bash
$ python -m pytest -k unittest
```