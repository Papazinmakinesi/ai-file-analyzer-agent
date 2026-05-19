import pytest
from src.text_processor import clean_text


def test_clean_text():
    result = clean_text("  Hello \n\n world ")
    assert result == "Hello world"


def test_empty_text():
    with pytest.raises(ValueError):
        clean_text("   ")


def test_non_string_input():
    with pytest.raises(TypeError):
        clean_text(123)