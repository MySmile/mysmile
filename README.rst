===========================
Lightweight CMS for Django
===========================

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

About
=====

MySmile is the lightweight open-source CMS based on Django. It helps to create websites with configurable design and minimum cost. 

* The official `project site <http://mysmile.com.ua>`_
* Try `demo version <http://demo.mysmile.com.ua>`_
* Read `documentation <http://http://mysmile.com.ua/en/documentation.html>`_
* `Source code <https://github.com/MySmile/MySmile>`_ on GitHub

Dependencies
============

a) `Django 1.8 <http://djangoproject.com>`_
b) `Pillow <https://python-pillow.github.io/>`_ for working with images
c) `Sphinx <http://sphinx-doc.org/>`_ for generate docs in various format

Installation
============

1. Unpack archive with MySmile to the project directory

2. Install with command: ``$ make install``

3. In the project directory run a command in the terminal:
    
  ``$ python3 manage.py runserver``
    
  Now your website is available here:
	
  `<http://127.0.0.1:8000>`_ 

4. Change default credentials to admin page:

4.1. Link to admin page:
      
  `<http://127.0.0.1:8000/admin>`_
      
4.2. Log in with default credentials:
  
  * login: *test*
  * password: *test*
