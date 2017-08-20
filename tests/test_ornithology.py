# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.ornithology import Instance
from duck.ornithology import ANY
from duck.compat import mock
import duck


def test_ornithology():
    mockint = duck.Mock(spec=int)
    mockfloat = duck.Mock(spec=float)
    assert mockint == Instance(int)
    assert mockfloat != Instance(int)
    assert mockint == ANY
    assert not mockint != ANY


def test_ornithology_compat():
    mockint = mock.Mock(spec=int)
    mockfloat = mock.Mock(spec=float)
    assert mockint == Instance(int)
    assert mockfloat != Instance(int)
    assert mockint == ANY
    assert not mockint != ANY
