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
    assert Instance(int) == 42
    assert Instance(int) != 2.718
    assert ANY == mockint
    assert not ANY != mockint
    assert ANY == "foo"
    assert not ANY != "foobar"
    assert repr(Instance(int)) == '<Instance: int>'


def test_ornithology_compat():
    mockint = mock.Mock(spec=int)
    mockfloat = mock.Mock(spec=float)
    assert mockint == Instance(int)
    assert Instance(int) != mockfloat
    assert Instance(int) == 42
    assert Instance(int) != 2.718
    assert ANY == mockint
    assert not ANY != mockint
    assert ANY == "foo"
    assert not ANY != "foobar"
    assert repr(Instance(int)) == '<Instance: int>'


def test_ornithology_science():
    """
    Reverse ordered test cases to find out if there's
    a specific incompatability in python 3.4
    :return:
    """
    mockint = duck.Mock(spec=int)
#    mockfloat = duck.Mock(spec=float)
#    assert mockint == Instance(int)
#    assert mockfloat != Instance(int)
    assert 42 == Instance(int)
    assert 2.718 != Instance(int)
    assert mockint == ANY
    assert not mockint != ANY
    assert "foo" == ANY
    assert not "foobar" != ANY
    assert repr(Instance(int)) == '<Instance: int>'
