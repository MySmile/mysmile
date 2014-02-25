Contact
-------

That resource [#f1]_ returns structured contact information such as phone, email, skype.

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

.. rubric:: Notes
.. [#f1] Parameters of response configurable through MySmile config file.