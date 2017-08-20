# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck.compat import mock


class Mock(mock.MagicMock):
    """A basic Mock object.

    When instantiated directly, this Mock is created with an empty spec, and
    is not substituted for any object. This is useful for passing as a callable
    to arguments and in some other situations.

    Args:
        name (str): The name of the mock. This is used in the ``repr`` of
            the mock and can be useful for debugging.
        spec (Union[tuple, Any]): The spec to use for this mock. If a tuple
            is provided, then the attributes specified therein are usable
            (and nothing else). If another object is provided, then its
            available attributes are used as the spec.
        side_effect (Union[Callable, Iterable]): A function to be called
            whenever the Mock is called. Useful for raising exceptions or
            dynamically changing return values. The function is called with the
            same arguments as the mock, and unless it returns
            :attr:`duck.DEFAULT`, the return value of this function is used as
            the return value.

            Alternatively, ``side_effect`` can be an exception class or
            instance. In this case the exception will be raised when the mock
            is called.

            If ``side_effect`` is an iterable then each call to the mock will
            return the next value from the iterable.
        return_value (Any): The return value for this mock if it is called.
            If not specified, then another :class:`duck.mocks.Mock` is
            returned.
        wraps (Callable): Item for the mock object to wrap. If wraps is not
            ``None`` then calling the Mock will pass the call through to the
            wrapped object (returning the real result). Attribute access on the
            mock will return a Mock object that wraps the corresponding
            attribute of the wrapped object (so attempting to access an
            attribute that does not exist will raise :exc:`AttributeError`).

            If both ``wraps`` and ``return_value`` are specified,
            ``return_value`` wins and ``wraps`` is ignored.
        kwargs (dict): Attributes to be set on the mock after it is created.
    """
    # def __init__(self, name=None, spec=(), side_effect=None,
    #              return_value=mock.DEFAULT, wraps=None, **kwargs):
    #     pass


class Stub(Mock):
    pass


class Spy(Stub):
    pass


__all__ = (
    'Mock',
    'Spy',
    'Stub',
)
