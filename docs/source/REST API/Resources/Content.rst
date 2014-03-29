Content
-------

That resource returns content of current page by slug or list of available contents.

.. list-table::
    :widths: 15 15 40
    :header-rows: 1

    * - Resource
      - GET [#f1]_ 
      - Example 
    * - /content
      - list of contents
      - ::
    
            {
                code: 200,
                data: {
                    "home":"Home",
                    "about":"About",
                    "contact":"Contact"
                }
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


.. rubric:: Notes
.. [#f1]  For other HTTP methods API response will returned error with 405 code. For more information see :ref:`Errors`  section.
