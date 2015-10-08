.. _faq:

**************************
Frequently Asked Questions
**************************

**Can I use the MySql database instead of SQLite?**

Yes. To do this, do the following:

#. Run :command:`$ pip3 install pymysql==0.6.7`
#. Add into *manage.py* lines ::
  import pymysql
  pymysql.install_as_MySQLdb()

befor line ::
  if __name__ == "__main__":
  
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

#. Run command :command:`$ make newdb`

#. Run local server  :command:`$ make run`
  