"""Module to test various algorithms"""
import pytest
from intellisense.algorithms import PrefixTree, PhoneticIndex


@pytest.fixture()
def prefix_tree_obj() -> PrefixTree:
    """Providing prefix tree object"""
    return PrefixTree({"example", "ekzampul"})


@pytest.fixture()
def phonetic_index_obj() -> PhoneticIndex:
    """Providing phonetic index object"""
    return PhoneticIndex({"example", "ekzampul"})


def test_prefix_tree(prefix_tree_obj):
    """Testing prefix tree built with custom vocabulary"""
    assert "example" in prefix_tree_obj.recommend("example")
    assert len(prefix_tree_obj.recommend("")) == 0
    assert len(prefix_tree_obj.recommend(None)) == 0


def test_phonetic_index(phonetic_index_obj):
    """Testing phonetic index built with custom vocabulary"""
    assert "example" in phonetic_index_obj.recommend("example")
    assert len(phonetic_index_obj.recommend("")) == 0
    assert len(phonetic_index_obj.recommend(None)) == 0
