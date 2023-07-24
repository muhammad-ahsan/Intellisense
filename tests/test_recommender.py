"""Module to tests various algorithms"""
import pytest

from intellisense.recommender import PhoneticRecommender


@pytest.fixture()
def phonetic_index() -> PhoneticRecommender:
    """Providing phonetic index object"""
    return PhoneticRecommender({"example", "ekzampul"})


def test_phonetic_index_recommend(phonetic_index):
    """Testing phonetic index built with custom vocabulary"""
    assert "example" in phonetic_index.get_recommendations("example")


@pytest.mark.parametrize(('input_n', 'expected'), (("", 0), (None, 0)))
def test_phonetic_index(phonetic_index, input_n, expected):
    assert len(phonetic_index.get_recommendations(input_n)) == expected
