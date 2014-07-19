Language
--------

That resource returns list of available languages.

.. tabularcolumns:: |p{3cm}|p{5cm}|p{7cm}|
.. list-table::
    :header-rows: 1

    * - Resource
      - GET
      - Example

    * - /language
      - list of supported languages
      - ::

          { code: 200, 
            data: ["ua","ru", "en"] 
            }
