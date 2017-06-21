================================================================================
sphinxcontrib-excel - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/sphinxcontrib-excel.svg?branch=master
   :target: http://travis-ci.org/pyexcel/sphinxcontrib-excel

.. image:: https://codecov.io/github/pyexcel/sphinxcontrib-excel/coverage.png
   :target: https://codecov.io/github/pyexcel/sphinxcontrib-excel



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


In order to update test environment, and documentation, additional steps are
required:

#. pip install moban
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is rnd_requirements.txt
-------------------------------

Usually, it is created when a dependent library is not released. Once the dependecy is installed(will be released), the future version of the dependency in the requirements.txt will be valid.

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows systems, please issue this command::

    > test.bat


License
================================================================================

New BSD License
