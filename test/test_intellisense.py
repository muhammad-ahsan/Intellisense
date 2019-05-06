import pytest

from intellisense import prefix_tree


@pytest.fixture
def my_prefix_tree():
    return prefix_tree()


def test_prefix_tree(my_prefix_tree):
    assert len(my_prefix_tree.recommend('')) == 0
