.. _User_configuration:

User configuration
==================

User configuration in *config/local.py* or *config/production.py* contains info of contact and general technical information.
    ::

      app_settings = {
	'PHONE': '000 000 000 00 00', 
	'EMAIL': 'myemail@email.com',
	'SKYPE': 'myskype',
	'GOOGLE_ANALITYCS_CODE': '',
	'MAX_INNERLINK_HISTORY': 4, 
	'REST_API': False
	}

The **MAX_INNERLINK_HISTORY** describes the maximum number of items of additional dynamic menu.

The **REST_API** allows you to globally enable/disable all pages accessible via API. 