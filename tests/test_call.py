import pytest
from duck.call import Call


def test_call_init():
    c = Call()
    assert c.args == []
    assert c.kwargs == {}

    c = Call('foo', 'bar', None, spam='egg', baz=None)
    assert c.args == ('foo', 'bar', None)
    assert c.kwargs == {
        'spam': 'egg',
        'baz': None,
    }


def test_call_has_args():
    c = Call('foo', 'bar', None, spam='egg', baz=None)

    # Validate args processing is correct.
    assert c.has_args('foo') is True
    assert c.has_args('bar') is False
    assert c.has_args('foo', 'bar') is True
    assert c.has_args(None) is False
    assert c.has_args('foo', None) is False
    assert c.has_args('foo', 'bar', None) is True
    assert c.has_args('foo', 'bar', None, 'baz') is False

    # Validate keyword args processing is correct.
    assert c.has_args(spam='egg') is True
    assert c.has_args(spam=None) is False
    assert c.has_args(baz=None) is True
    assert c.has_args(baz=1) is False
    assert c.has_args(spam='egg', baz=None) is True
    assert c.has_args(spam=None, baz=None) is False
    assert c.has_args(spam=None, baz=1) is False
    assert c.has_args(spam='egg', baz=None, way='cool') is False


def test_call_has_exact_args():
    c = Call('foo', 'bar', None, spam='egg', baz=None)

    assert c.has_exact_args('foo') is False
    assert c.has_exact_args('bar') is False
    assert c.has_exact_args('foo', 'bar') is False
    assert c.has_exact_args('bar', 'foo', None) is False
    assert c.has_exact_args('foo', 'bar', None) is False
    assert c.has_exact_args(way='cool') is False
    assert c.has_exact_args('foo', 'bar', None, spam='egg') is False
    assert c.has_exact_args('foo', 'bar', None, spam='egg', baz=None) is True
    assert c.has_exact_args('foo', 'bar', None, spam='egg', baz=1) is False
    assert c.has_exact_args('foo', 'bar', None, spam='egg',
                            baz=None, way='cool') is False


def test_call_assert_has_args():
    c = Call('foo', 'bar', None, spam='egg', baz=None)

    assert c.assert_has_args('foo') is True
    with pytest.raises(AssertionError):
        c.assert_has_args('bar')

    assert c.assert_has_args(spam='egg') is True
    with pytest.raises(AssertionError):
        c.assert_has_args(foo='bar')


def test_call_assert_has_exact_args():
    c = Call('foo', 'bar', None, spam='egg', baz=None)

    assert c.assert_has_exact_args('foo', 'bar', None, spam='egg',
                                   baz=None) is True

    with pytest.raises(AssertionError):
        c.assert_has_exact_args('foo')

    with pytest.raises(AssertionError):
        c.assert_has_exact_args('bar')

    with pytest.raises(AssertionError):
        c.assert_has_exact_args(None)

    with pytest.raises(AssertionError):
        c.assert_has_exact_args('foo', 'bar', None)

    with pytest.raises(AssertionError):
        c.assert_has_exact_args('bar', None, 'foo')

    with pytest.raises(AssertionError):
        c.assert_has_exact_args(spam='egg')

    with pytest.raises(AssertionError):
        c.assert_has_exact_args(baz=None)

    with pytest.raises(AssertionError):
        c.assert_has_exact_args(spam='egg', baz=None)

    with pytest.raises(AssertionError):
        c.assert_has_exact_args(spam=None, baz=1)
