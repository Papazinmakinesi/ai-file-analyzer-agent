import pytest
from src.file_reader import read_text_file


def test_read_valid_file():
    content = read_text_file("data/sample.txt")
    assert isinstance(content, str)
    assert len(content) > 0


def test_invalid_file_extension():
    with pytest.raises(ValueError):
        read_text_file("data/sample.pdf")


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_text_file("data/missing.txt")