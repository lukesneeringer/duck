# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import duck
from duck.compat import mock
from duck.ornithology import ANY
from duck.ornithology import Instance


def test_ornithology():
    mockint = duck.Mock(spec=int)
    mockfloat = duck.Mock(spec=float)
    assert Instance(int) == mockint
    assert Instance(int) != mockfloat
    assert ANY == mockint
    assert not ANY != mockint


def test_ornithology_compat():
    mockint = mock.Mock(spec=int)
    mockfloat = mock.Mock(spec=float)
    assert Instance(int) == mockint
    assert Instance(int) != mockfloat
    assert ANY == mockint
    assert not ANY != mockint
