{% extends "BASIC-README.rst.jj2" %}

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

Please add sphinxcontrib-excel into your conf.py file::

    extensions = [
	    ...
	    'sphinxcontrib.excel',
	    ...
	]

Here is the syntax to present your excel file in sphinx documentation::

    .. pyexcel-table:: filename.csv


For example, the following rst statment:

.. image:: sphinx-doc-source.png

is translated as:

.. image:: sphinx-doc-view.png

{%endblock%}
