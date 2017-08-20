# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

from duck import mocks
# from duck.compat import mock


def stub(target, attribute=None, create=False, spec=None,
         new_callable=mocks.Stub, **kwargs):
    """Replace the given target with a mock object or replacement callable.

    Ordinarily, the replacement object is a :class:`duck.Stub`, but if the
    ``new_callable`` argument is provided, then this class is used instead.

    Args:
        target (Union[Any, str]): The object to be patched. If ``attribute``
            is not set, then this is expected to be a string, and it is
            provided to :meth:`mock.patch`; if ``attribute`` is provided, then
            this is expected to be a class or module, and it is provided
            to :meth:`mock.patch.object`.
        attribute (str): The attribute to be replaced. Setting this attribute
            controls whether :meth:`mock.patch` or :meth:`mock.patch.object`
            is called under the hood.
        create (bool): If True, the attribute will be set even if it not
            already present. If False (the default), attempting to set a
            non-existent attribute will raise an exception.
        spec (Any): If ``None`` (the default), the object being patched is
            automatically used as the spec for the stub. If set to a tuple,
            then only the provided attribute names may be addressed. If set to
            an object, then that object is used as the spec. To forego a spec
            entirely, send ``False`` for this argument.
        new_callable (Callable): The callable to be used. If not provided,
            this is :class:`duck.mocks.Stub`.
        kwargs (dict): Any additional keyword arguments are passed to the
            callable.

    Returns:
        unittest.mock._patch: A patch object provided by mock.
    """
    # Determine the appropriate spec for the mock.
    # By default, this is autospec=True, unless a spec is provided or
    # explicitly turned off.
    if spec is None:
        kwargs['autospec'] = True
    elif spec is not False:
        kwargs['spec_set'] = spec

    # Place the `create` and `new_callable` arguments into **kwargs.
    kwargs['create'] = create
    kwargs['new_callable'] = new_callable

    # Return the appropriate mock function.
    if attribute is not None:
        return mock.patch.object(target, attribute, **kwargs)
    return mock.patch(target, **kwargs)


def spy(target, attribute):
    """Replace the given target with a spy object.

    The substitute object is a :class:`duck.Spy` object, which is a mock
    that will nonetheless route the actual calls to the original object.

    Args:
        target (Union[class, module]): This is expected to be a class or
            module, and it is provided to :meth:`mock.patch.object`.
        attribute (str): The attribute to be replaced.

    Returns:
        unittest.mock._patch: A patch object provided by mock.
    """
    spy_ = mocks.Spy(wraps=getattr(target, attribute), name=attribute)
    return mock.patch.object(target, attribute, new_callable=spy_)
