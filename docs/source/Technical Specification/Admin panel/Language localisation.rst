.. _Language_localisation:

Language localisation
---------------------

Add another language with option **LANGUAGES** in *mysmile/settings/base.py*. For example, this language will be 
polish. Create directory *pl* into directories:

* apps/pages/locale 
* apps/preferences/locale

Run command::
  $ make makemessages lang=pl

Open and translate files *locale/pl/LC_MESSAGES/django.po*, then run: ::
  $ make compilemessages

   