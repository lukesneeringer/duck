# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.compat import mock

# Contains the comparisons preserved from mock for use in asserts.

# Alias of mock.ANY
ANY = mock.ANY


class _Instance(object):
    """
    Instances of Instance have an .__eq__ method that returns
    True if and only if the other comparison object is an
    instance of the provided class (as defined by isinstance).
    """
    def __init__(self, _class):
        self._class = _class

    def __eq__(self, other):
        return isinstance(other, self._class)

    def __ne__(self, other):
        return not isinstance(other, self._class)

    def __repr__(self):
        return '<Instance>'

Instance = _Instance

__all__ = (
    'ANY',
    'Instance'
)