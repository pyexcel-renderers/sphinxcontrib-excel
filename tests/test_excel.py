import os
from mock import MagicMock
from sphinxcontrib.excel import PyexcelTable, setup as s
from nose.tools import eq_


def test_pyexcel_table_directive():
    arguments = [os.path.join("tests", "fixtures", "test.csv")]
    directive = PyexcelTable('test', arguments, None, None,
                             None, None, None, None, None)
    x = directive.run()
    content = str(x[0])
    assert '<raw format="html" xml:space="preserve">' in content
    assert 'var mydata = [[1, 2, 3]]' in content
    assert 'activateFirst' in content


def test_setup():
    app = MagicMock()
    ret = s(app)
    eq_(ret, {'version': '0.0.1'})
