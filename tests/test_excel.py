import os
from mock import MagicMock, patch
from sphinxcontrib.excel import setup as s
from nose.tools import eq_


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


def test_setup():
    app = MagicMock()
    ret = s(app)
    eq_(ret, {'version': '0.0.1'})
