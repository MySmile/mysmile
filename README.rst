Master:
  .. image:: https://travis-ci.org/MySmile/mysmile.svg?branch=master
    :target: https://travis-ci.org/MySmile/mysmile?branch=master
    :alt: Build

  .. image:: https://coveralls.io/repos/MySmile/mysmile/badge.svg?branch=master
    :target: https://coveralls.io/r/MySmile/mysmile?branch=master
    :alt: Test coverage

  .. image:: https://badge.fury.io/py/mysmile.svg
    :target: http://badge.fury.io/py/mysmile
    :alt: Pypi

  .. image:: https://readthedocs.org/projects/mysmile/badge/?version=stable
    :target: https://readthedocs.org/projects/mysmile/?badge=stable
    :alt: Documentation

Dev:
  .. image:: https://travis-ci.org/MySmile/mysmile.svg?branch=dev
    :target: https://travis-ci.org/MySmile/mysmile?branch=dev
    :alt: Build

  .. image:: https://coveralls.io/repos/MySmile/mysmile/badge.svg?branch=dev
    :target: https://coveralls.io/r/MySmile/mysmile?branch=dev
    :alt: Test coverage

  .. image:: https://readthedocs.org/projects/mysmile/badge/?version=dev
    :target: https://readthedocs.org/projects/mysmile/?badge=dev
    :alt: Documentation    

*******
MySmile
*******

MySmile is the lightweight open-source CMS based on Django. It helps to create websites with configurable design and minimum cost. 

* Official site `<http://mysmile.com.ua>`_
* Demo version `<http://demo.mysmile.com.ua>`_
* Documentation `<http://mysmile.com.ua/en/documentation.html>`_

Installation
============

#. Clone repository: ``git clone git@github.com:MySmile/mysmile.git``
#. Install dependencies: ``make install``
#. Run developing server: ``python3 manage.py runserver``
#. Open in browser: `<http://127.0.0.1:8000>`_
#. Change default admin credentials logging `<http://127.0.0.1:8000/admin>`_ by credentials: login - ``test``, password - ``test``

Requirements
============

- `Django 1.8 <http://djangoproject.com>`_
- `Pillow <https://python-pillow.github.io/>`_
- `Sphinx <http://sphinx-doc.org/>`_

Documentation
=============
- Technical documentation is available in `html <https://mysmile.readthedocs.org/en/latest/>`_
- Technical documentation source is in `docs </docs>`_

Docker
======
Instruction how to use Docker can be found in `Docker Readme </bin/docker>`_.

Tests
=====

Back-end unit
-------------
Python unit test can be found in ``tests`` folder inside each applications.

Running
```````
Manually:

- to run all tests execute ``make test``.
- to run specific test it's necessary set full path to test class. For instance: ``python3 manage.py test apps.chat.tests.test_views``.

With IDE:

All information to configure your IDE with Docker is in `Docker Readme </bin/docker>`_ using `PyCharm <https://www.jetbrains.com/pycharm/>`_ as an example.

Contribution
============
If you find this project worth to use please add a star. Follow changes to see all activities.
And if you see room for improvement, proposals please feel free to create an issue or send pull request.

Please note that this project is released with a `Contributor Code of Conduct <http://contributor-covenant.org/version/1/4/>`_.
By participating in this project and its community you agree to abide by those terms.

More information is in `Contributing <CONTRIBUTING.rst>`_.

License
=======
MySmile is licensed under the BSD 3-Clause License. Please see the `LICENSE <LICENSE.txt>`_ file for details.
