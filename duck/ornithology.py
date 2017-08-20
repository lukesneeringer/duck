# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.compat import mock

# Contains the comparisons preserved from mock for use in asserts.

# Alias of mock.ANY
ANY = mock.ANY


class Predicate(object):
    """An object considered to be equal to anything that passes its predicate function.

    Args:
        predicate (Callable): The predicate to use to test.
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
    """An object considered equal to any instance in which the compared
    value is contained within the presented object.

    Args:
        haystack (object): The object to be searched for the compared value
    """
    def __init__(self, haystack):
        self._object = haystack
        # todo: we may need to use a helper function to capture an AttributeError
        # or TypeError here, unless we're okay with the unhandled exceptions when
        # mismatching types
        super(Needle, self).__init__(lambda t: haystack.__contains__(t))

    def __repr__(self):
        return '<Needle: haystack: {0}>'.format(self._object)


__all__ = (
    'ANY',
    'Instance',
    'Predicate'
    'Needle'
)
