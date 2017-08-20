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
    """
     Instances of Needle have an .__eq__ method that returns
     True if and only if the provided needle is contained within
     the other comparison object (as defined by .__contains__).
     For example, it is true that quack.Needle('foo') == 'foobar'
    """
    def __init__(self, object_):
        self._object = object_
        # todo: we may need to use a helper function to capture an AttributeError
        # or TypeError here, unless we're okay with the unhandled exceptions when
        # mismatching types
        super(Needle, self).__init__(lambda t: object_.__contains__(t))

    def __repr__(self):
        return '<Needle: {0}>'.format(self._object)


__all__ = (
    'ANY',
    'Instance',
    'Predicate'
    'Needle'
)
