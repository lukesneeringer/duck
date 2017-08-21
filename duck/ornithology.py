# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.compat import mock

# Contains various comparators for use in mocks and tests

# Alias of mock.ANY
ANY = mock.ANY


class Predicate(object):
    """An object considered to be equal to anything that passes its predicate
    function.

    Args:
        predicate (Callable -> Bool): The predicate to use to test.
    """
    def __init__(self, predicate):
        self._predicate = predicate

    def __eq__(self, other):
        return self._predicate(other)

    def __ne__(self, other):
        return not self == other


class Instance(Predicate):
    """An object considered equal to any instance of the correct type.

    Args:
        class_ (type): The class to be checked against.
    """
    def __init__(self, class_):
        self._class = class_
        super(Instance, self).__init__(lambda t: isinstance(t, class_))

    def __repr__(self):
        return '<Instance: {0}>'.format(self._class.__name__)


class Needle(Predicate):
    """An object considered equal to any instance in which the presented value
    is contained within the compared object

    Args:
        needle (object): The object to search for within the compared object
    """
    def __init__(self, needle):
        self._object = needle
        super(Needle, self).__init__(lambda haystack: needle in haystack)

    def __repr__(self):
        return '<Needle: {0}>'.format(self._object)


__all__ = (
    'ANY',
    'Instance',
    'Predicate',
    'Needle',
)
