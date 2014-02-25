Errors
======

+-----------+---------------------------+-----------------------------------------------------------+
| HTTP code | Description               | Example                                                   |
+===========+===========================+===========================================================+
| 404       | Resource not found        | { code: 404, msg: "Not Found" }                           |
+-----------+---------------------------+-----------------------------------------------------------+
| 405       | Try to get access to POST | { code: 502, msg: "Method Not Allowed" }                  |
|           | if only GET available     |                                                           |
+-----------+---------------------------+-----------------------------------------------------------+
| 500       | Error in the code or      | { code: 500, msg: "Internal Server Error" }               |
|           |                           |                                                           |
|           | invalid parameters use    | { code: 500, msg: "Unsupported value of parameter lang" } |
+-----------+---------------------------+-----------------------------------------------------------+

Note: error messages should be only in English.

