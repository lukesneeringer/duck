# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.api import spy
from duck.api import stub
from duck.compat import mock
from duck.mocks import Mock
from duck.mocks import Spy
from duck.mocks import Stub
from duck.ornithology import ANY
from duck.ornithology import Instance
from duck.ornithology import Is
from duck.ornithology import Needle
from duck.ornithology import Predicate
from duck.ornithology import Regex

# Expose certain items in `mock` in our namespace.
DEFAULT = mock.DEFAULT
sentinel = mock.sentinel


__all__ = (
    'DEFAULT',
    'Mock',
    'sentinel',
    'Spy',
    'spy',
    'Stub',
    'stub',
    'ANY',
    'Instance',
    'Predicate',
    'Needle',
    'Regex',
    'Is',

)
