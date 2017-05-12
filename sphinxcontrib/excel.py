"""
    sphinxcontrib.excel
    ~~~~~~~~~~~~~~~~~~~~

    Embed excel file as an excel-alike table into sphinx documentation.

    :copyright: (c) 2017 by Onni Software Ltd.
    :license: New BSD, see LICENSE for details.
"""
from docutils.parsers.rst import Directive
from sphinx.util.i18n import search_image_for_language

import docutils.core
import pyexcel


class PyexcelTable(Directive):
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        env = self.state.document.settings.env
        fn = search_image_for_language(self.arguments[0], env)
        relfn, excel_file = env.relfn2path(fn)
        env.note_dependency(relfn)
        if len(self.arguments) == 2:
            width = self.arguments[1]
            width = width.split(' ')[-1]
            width = int(width)
        else:
            width = None
        sheet = pyexcel.get_book(file_name=excel_file)
        handsontable = sheet.get_handsontable_html(embed=True,
                                                   width=width)
        return [docutils.nodes.raw('', handsontable,
                                   format='html')]


def setup(app):
    app.add_directive('pyexcel-table', PyexcelTable)
    return {'version': '0.0.1'}
