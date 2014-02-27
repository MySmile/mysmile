Content
-------

That resource return content of current page by slug or list of available contents.


+-------------------+-------------------------+---------------------------------------------------+
| Resource          | GET [#f1]_              | Example                                           |
+===================+=========================+===================================================+
| /content          | list of contents        | { code: 200, data: ["home", "about", "contact"] } |
+-------------------+-------------------------+---------------------------------------------------+
| /content?slug=foo | current content by slug | {                                                 |
|                   |                         |  code: 200,                                       |
|                   |                         |  data: {                                          |
|                   |                         |    col_central: "html of central column",         |
|                   |                         |    col_right: "html of right column",             |
|                   |                         |    col_bottom: [                                  |
|                   |                         |        "html of first bottom column",             |
|                   |                         |        "html of second bottom column",            |
|                   |                         |        "html of third bottom column"              |
|                   |                         |          ],                                       |
|                   |                         |    photo: {                                       |
|                   |                         |    src: "url to photo",                           |
|                   |                         |    alt: "alt text",                               |
|                   |                         |    description: "description"                     |
|                   |                         |    }                                              |
|                   |                         |   }                                               |
|                   |                         | }                                                 |
+-------------------+-------------------------+---------------------------------------------------+


.. rubric:: Notes
.. [#f1]  For other HTTP methods API response will returned error with 405 code. For more information see :ref:`Errors`  section.



