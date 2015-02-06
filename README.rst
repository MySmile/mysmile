===========================
Lightweight CMS for Django
===========================

.. image:: https://badge.fury.io/py/mysmile.svg
   :target: http://badge.fury.io/py/mysmile
.. image:: https://coveralls.io/repos/MySmile/mysmile/badge.svg
   :target: https://coveralls.io/r/MySmile/mysmile     

MySmile is the lightweight open-source CMS based on Django. It helps to create websites with configurable design and minimum cost. 

* The official home page is `<http://mysmile.com.ua>`_
* Demo site is `<http://demo.mysmile.com.ua>`_

Dependencies
============
a) Django 1.7.x: http://djangoproject.com, https://github.com/django/django
b) PIL library for working with images: https://github.com/python-imaging/Pillow


Installation
============

1. Unpack archive with MySmile to the project directory

2. Install dependences: $ pip3 install -r config/requirements/local.txt

3. In the project directory run a command in the terminal: 
    
  `python3 manage.py runserver`
    
  Now your website is available here:
	
  `<http://127.0.0.1:8000>`_ 

4. Change default credentials to admin page:

  4.1. Link to admin page: 
      
  `<http://127.0.0.1:8000/admin>`_
      
  4.2. Log in with default credentials: 
  
  `login: test` 
  
  `password: test`

Documentation
=============
The latest documentation is available here `<http://mysmile.readthedocs.org/en/latest/>`_
