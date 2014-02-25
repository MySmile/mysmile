Contact
-------

That resource returns structured contact information such as phone, email, skype.

+-------------------+-------------------------+---------------------------------------------------+
| Resource          | GET                     | Example                                           |
+===================+=========================+===================================================+
| /contact          | list of contact data     | {                                                |
|                   |                          |  code: 200,                                      |
|                   |                          |  data: {                                         |
|                   |                          |     email: "test@mysmile.com",                   |
|                   |                          |     phone: "111-11-11",                          |
|                   |                          |     skype: "mysmile"                             |
|                   |                          |     }                                            |
|                   |                          |  }                                               |
+-------------------+--------------------------+--------------------------------------------------+

Note: parameters of response configurable through MySmile config file.
