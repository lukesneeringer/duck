# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from re import search
from re import MULTILINE
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


class Regex(Predicate):
    """An object considered equal to any object in which a valid regex
    can return at least one match. Uses a multiline search.

    Args:
        rex (str): the regular expression to be used to search the object
    """
    def __init__(self, rex):
        self._object = rex
        super(Regex, self).__init__(lambda other:
                                    search(rex, other, MULTILINE) is not None)

    def __repr__(self):
        return '<Regex: {0}>'.format(self._object)


class Is(Predicate):
    """An object considered equal if the compared object is the same
    object in memory.

    Args:
        object_ (object): The object to be checked.
    """
    def __init__(self, object_):
        self._object = object_
        super(Is, self).__init__(lambda other: object_ is other)

    def __repr__(self):
        return '<Is: {0}>'.format(self._object)


__all__ = (
    'ANY',
    'Instance',
    'Predicate',
    'Needle',
    'Regex',
    'Is',
)
