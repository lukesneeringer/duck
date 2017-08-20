# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import time

import pytest

import duck


def test_stub_context_manager():
    with duck.stub(time, 'sleep') as sleep:
        time.sleep(42)
        sleep.assert_called_once_with(42)
        with pytest.raises(AttributeError):
            sleep.bar


def test_stub_no_spec():
    with duck.stub(time, 'sleep', spec=False) as sleep:
        time.sleep(42)
        sleep.assert_called_once_with(42)

        # Since spec=False was sent, this should be acceptable.
        assert isinstance(sleep.bar, duck.Stub)
