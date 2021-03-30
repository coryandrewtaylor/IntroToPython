from flask_intro.util import _is_number


def test_int_is_number():
    assert _is_number("1")


def test_float_is_number():
    assert _is_number("1.0")


def test_str_is_not_number():
    assert not _is_number("a")