"""
    sphinxcontrib.excel
    ~~~~~~~~~~~~~~~~~~~~

    Embed excel file as an excel-alike table into sphinx documentation.

    :copyright: (c) 2017 by Onni Software Ltd.
    :license: New BSD, see LICENSE for details.
"""
from docutils.parsers.rst import Directive

import docutils.core
import pyexcel


class PyexcelTable(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        excel_file = self.arguments[0]
        sheet = pyexcel.get_book(file_name=excel_file)
        handsontable = sheet.get_handsontable_html(embed=True)
        return [docutils.nodes.raw('', handsontable,
                                   format='html')]


def setup(app):
    app.add_directive('pyexcel-table', PyexcelTable)
    return {'version': '0.0.1'}
