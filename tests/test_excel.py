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


@patch('sphinxcontrib.excel.search_image_for_language')
def test_pyexcel_table_directive(fake_search):
    from sphinxcontrib.excel import PyexcelTable
    state = MagicMock()
    fake_search.return_value = ''
    arguments = [os.path.join("tests", "fixtures", "test.csv")]
    state.document.settings.env.relfn2path.return_value = (None, arguments[0])
    directive = PyexcelTable('test', arguments, None, None,
                             None, None, None, state, None)
    x = directive.run()
    content = str(x[0])
    assert '<raw format="html" xml:space="preserve">' in content
    assert 'var mydata = [[1, 2, 3]]' in content
    assert 'activateFirst' in content


@patch('sphinxcontrib.excel.search_image_for_language')
def test_pyexcel_table_directive_with_width(fake_search):
    from sphinxcontrib.excel import PyexcelTable
    state = MagicMock()
    fake_search.return_value = ''
    arguments = [os.path.join("tests", "fixtures", "test.csv"), 'width: 600']
    state.document.settings.env.relfn2path.return_value = (None, arguments[0])
    directive = PyexcelTable('test', arguments, None, None,
                             None, None, None, state, None)
    x = directive.run()
    content = str(x[0])
    assert '<raw format="html" xml:space="preserve">' in content
    assert 'var mydata = [[1, 2, 3]]' in content
    assert 'activateFirst' in content


@patch('sphinxcontrib.excel.search_image_for_language')
def test_pyexcel_table_with_content(fake_search):
    from sphinxcontrib.excel import PyexcelTable
    state = MagicMock()
    fake_search.return_value = ''
    content = []
    with open(os.path.join("tests", "fixtures", "test.csv"), 'r') as f:
        content.append(f.readline())
    directive = PyexcelTable('test', [], None, content,
                             None, None, None, state, None)
    x = directive.run()
    content = str(x[0])
    assert '<raw format="html" xml:space="preserve">' in content
    assert 'var mydata = [[1, 2, 3]]' in content
    assert 'activateFirst' in content


def test_setup():
    app = MagicMock()
    ret = s(app)
    eq_(ret, {'version': '0.0.1'})
