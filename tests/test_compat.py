# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import six

from duck import compat


def test_mock():
    if six.PY3:
        from unittest import mock
        assert compat.mock is mock
    else:
        import mock
        assert compat.mock is mock
