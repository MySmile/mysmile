*************
Documentation
*************

For generating documentation it's used `Sphinx <http://www.sphinx-doc.org/>`_ with publishing in `Read the Docs <https://readthedocs.org/>`_.

Installation
============

Local
-----
Follow `instructions <http://www.sphinx-doc.org/en/1.4.9/install.html>`_ to install Sphinx.

Docker
------
Follow instructions in `Docker Readme <../bin/docker>`_.

Running
=======

Local
-----
To generate documentation please run commands bellow inside ``docs`` directory:

- to see all supported formats please run: ``make help``
- to get documentation in ``html`` format please run: ``make html``

*Note*: generated documentation is saved in ``docs/build`` directory.

Docker
------
Information how generate documentation using Spinx inside `Docker Readme <../bin/docker#sphinx>`_
