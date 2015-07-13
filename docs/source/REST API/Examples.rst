.. _Examples:

Examples
========


.. tabularcolumns:: |p{2.8cm}|p{12cm}
.. list-table::

    * - Request/GET
      - http://mysmile.com.ua/api/content?v=1&lang=en&format=json

    * - Response/Code
      - 200

    * - Response/Header
      - Content-Type application/json;

    * - Response/Body
      - ::

          {
            code: 200,
            data: [{"home":"Home"},
                   {"about":"About"},
                   {"contact":"Contact"}
                  ]
            }

