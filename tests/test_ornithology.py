# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import duck
from duck.compat import mock
from duck.ornithology import ANY
from duck.ornithology import Instance
from duck.ornithology import Needle


def test_ornithology_any():
    mockint = duck.Mock(spec=int)
    assert ANY == mockint
    assert not ANY != mockint
    assert ANY == "foo"
    assert not ANY != "foobar"
    # Reverse order tests
    # assert mockint == ANY # this test breaks in python 3.4
    # assert not mockfloat != ANY # this test breaks in python 3.4
    assert "foo" == ANY
    assert not "foobar" != ANY
    # Tests for compatibility with the original mock implementation.
    mockint = duck.Mock(spec=int)
    assert ANY == mockint
    assert not ANY != mockint


def test_ornithology_instance():
    mockint = duck.Mock(spec=int)
    mockfloat = duck.Mock(spec=float)
    assert Instance(int) == mockint
    assert Instance(int) != mockfloat
    assert Instance(int) == 42
    assert Instance(int) != 2.718
    assert repr(Instance(int)) == '<Instance: int>'
    # Reverse order tests
    # assert mockint == Instance(int) # this test breaks in python 3.4
    # assert mockfloat != Instance(int) # this test breaks in python 3.4
    assert 42 == Instance(int)
    assert 2.718 != Instance(int)
    # Tests for compatibility with the original mock implementation.
    mockint = mock.Mock(spec=int)
    mockfloat = mock.Mock(spec=float)
    assert mockint == Instance(int)
    assert Instance(int) != mockfloat


def test_ornithology_needle():
    """
    Tests for the needle
    :return:
    """
    try:
        collect = {"foo": "bar", "baz": 1}
        word = "quack"
        value_list = [1, 2, "five"]
        assert Needle(collect) == "foo"
        assert Needle(word) == "ack"
        assert not Needle(word) == "duck"
        assert Needle(value_list) == 1
        assert Needle(value_list) == "five"
        assert not Needle(value_list) == 3
        assert repr(Needle(value_list)) == "<Needle: haystack: [1, 2, 'five']>"
    except AttributeError as ae:
        print(ae)
        assert False
