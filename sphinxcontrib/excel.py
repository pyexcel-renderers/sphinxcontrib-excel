"""
    sphinxcontrib.excel
    ~~~~~~~~~~~~~~~~~~~~

    Embed excel file as an excel-alike table into sphinx documentation.

    :copyright: (c) 2017 by Onni Software Ltd.
    :license: New BSD, see LICENSE for details.
"""
from docutils.parsers.rst import Directive
from sphinx.util.i18n import search_image_for_language
from docutils.parsers.rst import directives

import docutils.core
import pyexcel


class PyexcelTable(Directive):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int
    }

    def run(self):
        env = self.state.document.settings.env
        width = 600
        height = None

        if len(self.arguments) > 0:
            fn = search_image_for_language(self.arguments[0], env)
            relfn, excel_file = env.relfn2path(fn)
            env.note_dependency(relfn)
            if self.options:
                width = self.options.get('width', 600)
                height = self.options.get('height')
            book = pyexcel.get_book(file_name=excel_file)
        else:
            content = '\n'.join(self.content)
            if '---pyexcel' in content:
                multiple_sheets = True
            else:
                multiple_sheets = False
            book = pyexcel.get_book(file_content='\n'.join(self.content),
                                    multiple_sheets=multiple_sheets,
                                    lineterminator='\n',
                                    file_type='csv')
        html = self.render_html(book, width, height)
        return [docutils.nodes.raw('', html,
                                   format='html')]

    def render_html(self, book, width, height):
        return book.get_handsontable_html(
            embed=True, width=width, height=height)


class Pyecharts(PyexcelTable):

    def render_html(self, book, width, height):
        return book.get_echarts_html(embed=True,
                                     height=height,
                                     width=width)


def setup(app):
    app.add_directive('pyexcel-table', PyexcelTable)
    app.add_directive('pyexcel-echarts', Pyecharts)
    return {'version': '0.0.1'}
