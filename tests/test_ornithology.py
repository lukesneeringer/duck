# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import duck
from duck.compat import mock
from duck.ornithology import ANY
from duck.ornithology import Instance
from duck.ornithology import Needle


def test_ornithology_any():
    """
    Tests for ANY alias.
    """
    mockint = duck.Mock(spec=int)
    assert ANY == mockint
    assert not ANY != mockint
    assert ANY == "foo"
    assert not ANY != "foobar"
    # Reverse order tests
    assert "foo" == ANY
    assert not "foobar" != ANY
    # Tests for compatibility with the original mock implementation.
    mockint = duck.Mock(spec=int)
    assert ANY == mockint
    assert not ANY != mockint


def test_ornithology_instance():
    """
    Tests for the Instance comparator
    """
    mockint = duck.Mock(spec=int)
    mockfloat = duck.Mock(spec=float)
    assert Instance(int) == mockint
    assert Instance(int) != mockfloat
    assert Instance(int) == 42
    assert Instance(int) != 2.718
    assert repr(Instance(int)) == '<Instance: int>'
    # Reverse order tests
    assert 42 == Instance(int)
    assert 2.718 != Instance(int)
    # Tests for compatibility with the original mock implementation.
    mockint = mock.Mock(spec=int)
    mockfloat = mock.Mock(spec=float)
    assert mockint == Instance(int)
    assert Instance(int) != mockfloat


def test_ornithology_needle():
    """
    Tests for the needle comparator
    """
    collect = {"foo": "bar", "baz": 1}
    word = "quack"
    value_list = [1, 2, "five"]
    assert Needle("foo") == collect
    assert Needle("ack") == word
    assert not Needle("duck") == word
    assert Needle(1) == value_list
    assert Needle("five") == value_list
    assert not Needle(3) == value_list
    assert repr(Needle("foo")) == "<Needle: foo>"


def test_ornithology_regex():
    """
    Tests for regex comparisons
    """
    pass


def test_ornithology_is():
    """
    Tests for Is comparisons
    """
    pass

