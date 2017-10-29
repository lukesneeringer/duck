# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import duck
from duck.compat import mock
from duck.ornithology import ANY
from duck.ornithology import Instance
from duck.ornithology import Is
from duck.ornithology import Needle
from duck.ornithology import Regex


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
    searched_string = "The Quick Brown Fox Jumped\nover the Lazy Dog"
    searched_string_b = "The Quick Purple Fox Jumped\nover the Lazy Dog"
    assert Regex('^over the .azy Dog$') == searched_string
    assert searched_string_b == Regex('Quick (.+?) Fox')
    assert not Regex('Quick (.+?) Frog') == searched_string_b
    assert repr(Regex('Quick (.+?) Frog')) == "<Regex: Quick (.+?) Frog>"


def test_ornithology_is():
    """
    Tests for Is comparisons
    """
    mockfloat = duck.Mock(spec=float)
    duckfloat = mockfloat
    testobject = object()
    string_a = "Test"
    string_b = "Test"
    assert Is(mockfloat) == duckfloat
    assert not Is(duckfloat) == testobject
    assert Is(string_a) == string_b
    assert not Is(string_a + string_b) == string_b
    assert Is(2+2) == 4
    assert not Is(2+2) == 5
    assert repr(Is(string_a)) == "<Is: Test>"
