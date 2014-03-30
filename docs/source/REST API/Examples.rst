.. _Examples:


Examples
========

.. list-table::
    :widths: 40 15 25 40
    :header-rows: 1

    * - Request/GET
      - Response/Code
      - Response/Header
      - Response/Body

    * - http://mysmile.com.ua/api/content?v=1&lang=en&format=json
      - 200
      - Content-Type application/json;
      - ::

            {
                code: 200,
                data: {
                    10: {"home":"Home"},
                    20: {"about":"About"},
                    30: {"contact":"Contact"}
                }
            }
