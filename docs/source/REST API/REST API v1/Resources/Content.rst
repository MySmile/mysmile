Content
-------

That resource returns content of current page by slug or list of available contents if slug is not set.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|p{10.5cm}|
.. list-table::
    :header-rows: 1

    * - Resource
      - GET [#f1]_ 
      - Example 

    * - /content
      - list of contents
      - ::
    
          {
            code: 200,
            data: [{"home":"Home"},
                  {"about":"About"},
                  {"contact":"Contact"}
                ]
          }

    * - /content?slug=foo
      - current content by slug
      - ::

          {
            code: 200, 
            data: {
              menu: "Home",
              name: "name of central column",
              col_central: "html of central column", 
              col_right: "html of right column", 
              col_bottom: [
                "html of first bottom column",
                "html of second bottom column", 
                "html of third bottom column"
                ],
              youtube: "link to YouTube resource",
              photo: { 
                    src: "url to photo", 
                    alt: "alt text", 
                    description: "description" 
              }
            }
          }


.. rubric:: Footnotes

.. [#f1]  For other HTTP methods API response will returned error with 405 code. For more information please see :ref:`Errors`  section.
