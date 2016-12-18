.. _faq:

**************************
Frequently Asked Questions
**************************

**Can I use the MySql database instead of SQLite?**

Yes. To do this please follow:

#. Run ``$ pip3 install pymysql==0.6.7``
#. Add into *manage.py* this lines before line ``if __name__ == "__main__":``::

    import pymysql
    pymysql.install_as_MySQLdb()

#. Set Django DATABASES settings in *config/local.py* like ::

     DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'mysmile',
           'USER': 'root',
           'PASSWORD': 'password',
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
     }
#. Create database *mysmile*
#. Run command ``$ make newdb``
#. Run local server ``$ make run``
