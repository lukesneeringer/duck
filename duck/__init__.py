# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.api import stub
from duck.compat import mock
from duck.mocks import MagicMock
from duck.mocks import Mock
from duck.mocks import Spy
from duck.mocks import Stub

# Expose certain items in `mock` in our namespace.
DEFAULT = mock.DEFAULT
sentinel = mock.sentinel


__all__ = (
    'DEFAULT',
    'MagicMock',
    'Mock',
    'sentinel',
    'Spy',
    'Stub',
)
