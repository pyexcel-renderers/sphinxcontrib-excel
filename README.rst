================================================================================
sphinxcontrib-excel - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/sphinxcontrib-excel.svg?branch=master
   :target: http://travis-ci.org/pyexcel/sphinxcontrib-excel

.. image:: https://codecov.io/gh/pyexcel/sphinxcontrib-excel/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyexcel/sphinxcontrib-excel

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby


Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please `support me on patreon <https://www.patreon.com/bePatron?u=5537627>`_ to
maintain the project and develop it further.

If you are an individual, you are welcome to support me too on patreon and for however long
you feel like to. As a patreon, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.



Introduction
================================================================================
**sphinxcontrib-excel** uses pyexcel to read an excel files and renders into an excel-alike sheet in your sphinx documentation. The excel file formats are:

#. csv
#. tsv
#. csvz
#. tsvz
#. xls
#. xlsx
#. xlsm
#. ods




Installation
================================================================================
You can install it via pip:

.. code-block:: bash

    $ pip install sphinxcontrib-excel


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/sphinxcontrib-excel.git
    $ cd sphinxcontrib-excel
    $ python setup.py install



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



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/sphinxcontrib-excel.git
#. cd sphinxcontrib-excel

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt

Once you have finished your changes, please provide test case(s), relevant documentation
and update CHANGELOG.rst.

.. note::

    As to rnd_requirements.txt, usually, it is created when a dependent
    library is not released. Once the dependecy is installed
    (will be released), the future
    version of the dependency in the requirements.txt will be valid.


How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows systems, please issue this command::

    > test.bat

How to update test environment and update documentation
---------------------------------------------------------

Additional steps are required:

#. pip install moban
#. git clone https://github.com/moremoban/setupmobans.git # generic setup
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

Acceptance criteria
-------------------

#. Has Test cases written
#. Has all code lines tested
#. Passes all Travis CI builds
#. Has fair amount of documentation if your change is complex
#. Please update CHANGELOG.rst
#. Please add yourself to CONTRIBUTORS.rst
#. Agree on NEW BSD License for your contribution



License
================================================================================

New BSD License
