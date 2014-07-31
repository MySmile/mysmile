.. _Errors:

Errors
======

.. tabularcolumns:: |p{2.5cm}|p{5cm}|p{7.5cm}|
.. list-table::
    :header-rows: 1

    * - HTTP code
      - Description
      - Example [#f1]_
    * - 403
      - Request was a valid one, but server was refusing to respond to it.
      - ::
        
          { code: 403, 
            msg: "Forbidden"
            }
    * - 404
      - Resource not found.
      - ::
        
          { code: 404, 
            msg: "Not Found" 
            }
    * - 405
      - A request was made of a resource using a request method not supported by that resource. Try to get access to POST if only GET available.
      - ::
        
          { code: 405, 
            msg: "Method Not Allowed" 
            } 
    * - 500
      - A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. Error in the code or invalid parameters use.
      - ::
        
          { code: 500, 
            msg: "Internal Server Error"
            }
    * - 501
      - The server either does not recognize the request method, or it lacks the ability to fulfill the request. Resource does not implemented
      - ::
        
          { code: 501, 
            msg: "Not Implemented" 
            }


.. rubric:: Footnotes

.. [#f1] Error messages should be only in English.

