===========================
Lightweight CMS for Django
===========================

.. image:: https://badge.fury.io/py/mysmile.svg
    :target: http://badge.fury.io/py/mysmile
.. image:: https://travis-ci.org/MySmile/mysmile.svg?branch=dev
    :target: https://travis-ci.org/MySmile/mysmile   
.. image:: https://coveralls.io/repos/MySmile/mysmile/badge.svg?branch=dev
    :target: https://coveralls.io/r/MySmile/mysmile?branch=dev     

MySmile is the lightweight open-source CMS based on Django. It helps to create websites with configurable design and minimum cost. 

* The official home page is `<http://mysmile.com.ua>`_
* Demo site is `<http://demo.mysmile.com.ua>`_
* The documentation is available here `<http://http://mysmile.com.ua/en/documentation.html>`_

Dependencies
============
a) Django 1.8.x: http://djangoproject.com, https://github.com/django/django
b) Pillow for working with images: https://github.com/python-imaging/Pillow
c) Sphinx for generate docs in various format

Installation
============

1. Unpack archive with MySmile to the project directory

2. Install with command: `$ make install`

3. In the project directory run a command in the terminal: 
    
  `$ python3 manage.py runserver`
    
  Now your website is available here:
	
  `<http://127.0.0.1:8000>`_ 

4. Change default credentials to admin page:

4.1. Link to admin page:
      
  `<http://127.0.0.1:8000/admin>`_
      
4.2. Log in with default credentials:
  
  `login: test` 
  
  `password: test`


