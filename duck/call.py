class Call(object):
    """A Call object.

    A representation of a call made against a ``Mock`` object. It is
    similar to :class:`unittest.mock._Call`, but is designed to be more
    easily reasoned about.

    Args:
        args (list): Positional arguments provided to the call.
        kwargs (dict): Keyword arguments provided to the call.
    """
    def __init__(self, *args, **kwargs):
        self.args = []
        if args:
            self.args = args

        self.kwargs = {}
        if kwargs:
            self.kwargs = kwargs

    def has_args(self, *args, **kwargs):
        """Returns ``True`` if the call was made with a superset of the provided
        arguments and keyword arguments, and ``False`` otherwise.

        If provided, positional arguments must start at ``0`` and be in order.

        Comparisons are performed with ``==``, not ``is``.
        """
        results = []

        # If the given arguments exceed the number of actual arguments, this
        # cannot be true, and we can stop here.
        if len(args) > len(self.args):
            return False

        # Determine if the given argument(s) are present in the Call.
        args_results = []
        for idx, actual in enumerate(args):
            if actual == self.args[idx]:
                args_results.append(True)
            else:
                args_results.append(False)

        results.append(all(args_results))

        # If the given keyword arguments exceed the number of actual keyword
        # arguments, this cannot be true either.
        if len(kwargs) > len(self.kwargs):
            return False

        # Determine if the given keyword argument(s) are present in the Call.
        kwargs_results = []
        for k, v in kwargs.items():
            if k in self.kwargs and self.kwargs[k] == v:
                kwargs_results.append(True)
            else:
                kwargs_results.append(False)

        results.append(all(kwargs_results))

        return all(results)

    def has_exact_args(self, *args, **kwargs):
        """Returns ``True`` if the call was made with exactly the provided
        arguments and keyword arguments, and ``False`` otherwise.

        If provided, positional arguments must start at ``0`` and be in order.

        Comparisons are performed with ``==``, not ``is``.
        """
        # There must be the same number of arguments.
        if len(args) != len(self.args):
            return False

        # Arguments must be identical.
        for idx, actual in enumerate(args):
            if actual != self.args[idx]:
                return False

        # There must be the same number of keyword arguments.
        if len(kwargs) != len(self.kwargs):
            return False

        # They must be identical.
        for k, v in kwargs.items():
            if k not in self.kwargs or self.kwargs[k] != v:
                return False

        return True

    def assert_has_args(self, *args, **kwargs):
        """Calls the ``has_args`` method, and raises ``AssertionError``
        if ``False`` is returned.
        """
        errors = []

        # Determine if the given arguments are valid.
        if not self.has_args(*args):
            errors.append('Given args: {} != Valid args: {}'.format(
                args,
                self.args,
            ))

        # Determine if the given keyword arguments are valid.
        if not self.has_args(**kwargs):
            errors.append('Given kwargs: {} != Valid kwargs: {}'.format(
                kwargs,
                self.kwargs,
            ))

        if errors:
            raise AssertionError('\r\n'.join(errors))

        return True

    def assert_has_exact_args(self, *args, **kwargs):
        """Calls the ``has_exact_args`` method, and raises ``AssertionError``
        if ``False`` is returned.

        In order to return useful debugging information, it post-processes
        similar to ``has_exact_args``, but with additional information.
        """
        errors = []

        # Determine if the full set of (kw)arguments is valid.
        if not self.has_exact_args(*args, **kwargs):

            # There must be the same number of arguments.
            if len(args) != len(self.args):
                errors.append('Given args: {} != Actual args: {}'.format(
                    args,
                    self.args,
                ))
            else:
                # Arguments must be identical.
                args_error = False
                for idx, actual in enumerate(args):
                    if actual != self.args[idx]:
                        args_error = True

                if args_error:
                    errors.append('Given args: {} != Actual args: {}'.format(
                        args,
                        self.args,
                    ))

            # There must be the same number of keyword arguments.
            if len(kwargs) != len(self.kwargs):
                errors.append('Given kwargs: {} != Actual kwargs: {}'.format(
                    kwargs,
                    self.kwargs,
                ))
            else:
                # They must be identical.
                kwargs_error = False
                for k, v in kwargs.items():
                    if k not in self.kwargs or self.kwargs[k] != v:
                        kwargs_error = True

                if kwargs_error:
                    errors.append(
                        'Given kwargs: {} != Actual kwargs: {}'.format(
                            kwargs,
                            self.kwargs,
                        )
                    )

        if errors:
            raise AssertionError('\r\n'.join(errors))

        return True
