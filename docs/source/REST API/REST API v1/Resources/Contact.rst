Contact
-------

That resource [#f1]_ returns structured contact information such as phone, email, skype.

.. tabularcolumns:: |p{2.5cm}|p{4cm}|p{8.5cm}|
.. list-table::
    :header-rows: 1

    * - Resource
      - GET
      - Example

    * - /contact
      - list of contact data
      - ::

          {
            code: 200,
            data: {
              email: "test@mysmile.com",
              phone: "111-11-11",
              skype: "mysmile"
            }
          }

.. rubric:: Notes
.. [#f1] Parameters of response configurable through MySmile settings table in database (since v 0.5.0 of api sever).
