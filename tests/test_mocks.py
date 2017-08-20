# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import duck
from duck.compat import mock


def test_mock():
    m = duck.Mock()

    # Is this what we think it is?
    assert isinstance(m, mock.MagicMock)

    # Do extremely basic mock tests.
    assert not m.called
    m(foo='bar')
    m.assert_called_once_with(foo='bar')
