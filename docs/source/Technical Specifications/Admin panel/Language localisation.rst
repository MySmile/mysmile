.. _Language_localisation:

Language localisation
---------------------

To add new localisation please use option **LANGUAGES** in *mysmile/settings/base.py*.

For example, for Polish create directory *pl* in *mysmile/locale/*

Run command::

  $ make makemessages lang=pl

Open and translate files *locale/pl/LC_MESSAGES/django.po*, then run::
  
  $ make compilemessages lang=pl

   