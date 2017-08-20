# Copyright 2017 Luke Sneeringer
# Distributed under the MIT License (http://opensource.org/licenses/MIT)

import json
import logging

import pytest

import duck


def test_stub_context_manager():
    with duck.stub(json, 'dumps') as dumps:
        json.dumps({'foo': 42})
        dumps.assert_called_once_with({'foo': 42})
        with pytest.raises(AttributeError):
            dumps.bar


def test_stub_no_spec():
    with duck.stub(json, 'dumps', spec=False) as dumps:
        json.dumps({'foo': 42})
        dumps.assert_called_once_with({'foo': 42})

        # Since spec=False was sent, this should be acceptable.
        assert isinstance(dumps.bar, duck.Stub)


def test_stub_explicit_spec():
    with duck.stub(logging, 'Logger', spec=['info']) as mock_logger:
        mock_logger.return_value = mock_logger
        logger = logging.Logger()
        logger.info('foo')
        with pytest.raises(AttributeError):
            logger.error('bar')
        mock_logger.info.assert_called_once_with('foo')


def test_stub_string_only():
    with duck.stub('json.dumps') as dumps:
        json.dumps({'foo': 42})
        dumps.assert_called_once_with({'foo': 42})


def test_spy():
    with duck.spy(json, 'dumps') as dumps:
        # The actual json.dumps method will raise TypeError if it gets
        # unrecognized objects.
        with pytest.raises(TypeError):
            json.dumps({'foo': duck.sentinel.NO_SERIALIZATION})
        dumps.assert_called_once_with({'foo': duck.sentinel.NO_SERIALIZATION})
