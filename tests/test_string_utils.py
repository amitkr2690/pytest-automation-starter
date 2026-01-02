from utils.string_utils import reverse_string
import pytest

def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_error():
    with pytest.raises(ValueError):
        reverse_string(123)
