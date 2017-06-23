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

And you will need to copy a few resources file to your sphinx source directory::

    resources/_template/layout.html
    resources/_static/handsontable.full.min.js
    resources/_static/handsontable.full.min.css

.. note::

   `resources` directory is in github. please check it out.

Here is the syntax to present your excel file in sphinx documentation::

    .. pyexcel-table:: filename.csv

And 'filename.csv' is expected in the directory where the referring rst file is.
Relative path needs to be given if your file is somewhere else.

For example, the following rst statment:

.. image:: https://github.com/pyexcel/sphinxcontrib-excel/raw/master/sphinx-doc-source.png
   :alt: table directive

is translated as:

.. image:: https://github.com/pyexcel/sphinxcontrib-excel/raw/master/sphinx-doc-view.png
   :alt: table view

Embed csv into your sphinx documentation
--------------------------------------------------

Here is the syntax for embedded csv, `rendering as a single handsontable <http://pyexcel.readthedocs.io/en/latest/#usage>`_:

.. code-block::

   .. pyexcel-table::

      ---pyexcel:example table---
      Name,Age
      Adam,28
      Beatrice,29
      Ceri,30
      Dean,26  

Here is the complex example for embedded csv, which will be `rendered as
multi-tab handsontable <http://pyexcel.readthedocs.io/en/latest/tutorial_data_conversion.html#how-to-obtain-a-dictionary-from-a-multiple-sheet-book>`_):


.. code-block::

   .. pyexcel-table::

      ---pyexcel:Sheet 1---
      1,2,3
      4,5,6
      7,8,9
      ---pyexcel---
      ---pyexcel:Sheet 2---
      X,Y,Z
      1,2,3
      4,5,6
      ---pyexcel---
      ---pyexcel:Sheet 3---
      O,P,Q
      3,2,1
      4,3,2


{%endblock%}
