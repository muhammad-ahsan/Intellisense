"""Module to tests various algorithms"""
import pytest

from intellisense.algorithms import PhoneticIndex


@pytest.fixture()
def phonetic_index() -> PhoneticIndex:
    """Providing phonetic index object"""
    return PhoneticIndex({"example", "ekzampul"})


def test_phonetic_index_recommend(phonetic_index):
    """Testing phonetic index built with custom vocabulary"""
    assert "example" in phonetic_index.get_recommendations("example")


@pytest.mark.parametrize(('input_n', 'expected'), (("", 0), (None, 0)))
def test_phonetic_index(phonetic_index, input_n, expected):
    assert len(phonetic_index.get_recommendations(input_n)) == expected
