{% extends "BASIC-README.rst.jj2" %}

{%block documentation_link%}
{%endblock%}

{%block constraint%}
{%endblock%}

{%block features %}
**{{name}}** uses pyexcel to read an excel files and renders into an excel-alike sheet in your sphinx documentation. The excel file formats are:

   #. csv
   #. tsv
   #. csvz
   #. tsvz
   #. xls
   #. xlsx
   #. xlsm
   #. ods

{%endblock%}

{%block usage%}

Setup
================================================================================

Please add sphinxcontrib-excel into your conf.py file::

    extensions = [
	    ...
	    'sphinxcontrib.excel',
	    ...
	]

Here is the syntax to present your excel file in sphinx documentation::

    .. pyexcel-table:: filename.csv

And 'filename.csv' is expected in the director where the referring rst file is.
Relative path needs to be given if your file is somewhere else.

For example, the following rst statment:

.. image:: https://github.com/pyexcel/sphinxcontrib-excel/blob/master/sphinx-doc-source.png
   :alt: table directive

is translated as:

.. image:: https://github.com/pyexcel/sphinxcontrib-excel/blob/master/sphinx-doc-view.png
   :alt: table view

{%endblock%}
