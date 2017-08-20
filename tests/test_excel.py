import os
from mock import MagicMock, patch
from sphinxcontrib.excel import setup as s
from nose.tools import eq_

"""
    When a directive implementation is being run, the directive class
    is instantiated, and the `run()` method is executed.  During
    instantiation, the following instance variables are set:

    - ``name`` is the directive type or name (string).

    - ``arguments`` is the list of positional arguments (strings).

    - ``options`` is a dictionary mapping option names (strings) to
      values (type depends on option conversion functions; see
      `option_spec` above).

    - ``content`` is a list of strings, the directive content line by line.

    - ``lineno`` is the line number of the first line of the directive.

    - ``content_offset`` is the line offset of the first line of the
      content from
      the beginning of the current input.  Used when initiating a nested parse.

    - ``block_text`` is a string containing the entire directive.

    - ``state`` is the state which called the directive function.

    - ``state_machine`` is the state machine which controls the state
      which called
      the directive function.
"""


def _verify_result(directive_run_result):
    content = str(directive_run_result[0])
    assert '<raw format="html" xml:space="preserve">' in content
    assert 'var mydata = [[1, 2, 3]]' in content
    assert 'activateFirst' in content
    return content


class TestTableDirective:
    def setUp(self):
        self.patcher = patch('sphinxcontrib.excel.search_image_for_language')
        fake_search = self.patcher.start()
        fake_search.return_value = ''

    def tearDown(self):
        self.patcher.stop()

    def test_pyexcel_table_directive(self):
        from sphinxcontrib.excel import PyexcelTable
        state = MagicMock()
        arguments = [os.path.join("tests", "fixtures", "test.csv")]
        state.document.settings.env.relfn2path.return_value = (
            None, arguments[0])
        directive = PyexcelTable('test', arguments, None, None,
                                 None, None, None, state, None)
        result = directive.run()
        _verify_result(result)

    def test_pyexcel_table_directive_with_width(self):
        from sphinxcontrib.excel import PyexcelTable
        state = MagicMock()
        arguments = [os.path.join("tests", "fixtures", "test.csv")]
        options = {'width': 400}
        state.document.settings.env.relfn2path.return_value = (
            None, arguments[0])
        directive = PyexcelTable('test', arguments, options, None,
                                 None, None, None, state, None)
        result = directive.run()
        content = _verify_result(result)
        # make sure with 400 takes effect
        assert '<ul class="tab" style="width:400px;">' in content

    def test_pyexcel_table_with_content(self):
        from sphinxcontrib.excel import PyexcelTable
        state = MagicMock()
        content = []
        with open(os.path.join("tests", "fixtures", "test.csv"), 'r') as f:
            content.append(f.readline())
        directive = PyexcelTable('test', [], None, content,
                                 None, None, None, state, None)
        result = directive.run()
        _verify_result(result)

    def test_pyexcel_table_with_multiple_sheet_content(self):
        from sphinxcontrib.excel import PyexcelTable
        state = MagicMock()
        content = [
            '---pyexcel:Sheet 1---',
            '1,2,3',
            '4,5,6',
            '7,8,9',
            '---pyexcel---',
            '---pyexcel:Sheet 2---',
            'X,Y,Z',
            '1,2,3',
            '4,5,6',
            '---pyexcel---',
            '---pyexcel:Sheet 3---',
            'O,P,Q',
            '3,2,1',
            '4,3,2',
        ]
        directive = PyexcelTable('test', [], None, content,
                                 None, None, None, state, None)
        result = directive.run()
        result = str(result[0])
        assert '<raw format="html" xml:space="preserve">' in result
        assert '[["O", "P", "Q"], [3, 2, 1], [4, 3, 2]];' in result
        assert '[["X", "Y", "Z"], [1, 2, 3], [4, 5, 6]];' in result
        assert '[[1, 2, 3], [4, 5, 6], [7, 8, 9]];' in result
        assert 'activateFirst' in result


def test_setup():
    app = MagicMock()
    ret = s(app)
    eq_(ret, {'version': '0.0.1'})
