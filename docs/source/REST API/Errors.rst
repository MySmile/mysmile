.. _Errors:

Errors
======

+-----------+-------------------------------+-----------------------------------------------------------+
| HTTP code | Description                   | Example                                                   |
+===========+===============================+===========================================================+
| 404       | Resource not found            | { code: 404, msg: "Not Found" } [#f1]_                    |
+-----------+-------------------------------+-----------------------------------------------------------+
| 405       | Try to get access to POST     | { code: 502, msg: "Method Not Allowed" }                  |
|           | if only GET available         |                                                           |
+-----------+-------------------------------+-----------------------------------------------------------+
| 500       | Error in the code or          | { code: 500, msg: "Internal Server Error" }               |
|           | invalid parameters use        |                                                           |
|           |                               | { code: 500, msg: "Unsupported value of parameter lang" } |
+-----------+-------------------------------+-----------------------------------------------------------+
| 501       | Resource does not implemented | { code: 501, msg: "Not Implemented" }                     |
+-----------+-------------------------------+-----------------------------------------------------------+

.. rubric:: Notes
.. [#f1] Error messages should be only in English.

