Request
=======

Request format is: endpoint + resource + required parameters. General parameters can be omitted because they have default values.
For instance request to get content with slug *home* in *json* format with *en* language:

``/content?slug=home&v=1&lang=en&format=json``

The same but with omitted general parameters: 

``/content?slug=home``

Request to get list of all contents:

``/content``

See :ref:`Examples` for details.
