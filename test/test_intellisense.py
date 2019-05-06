from intellisense import prefix_tree


def test_prefix_tree():
    assert len(prefix_tree.recommend('')) == 0
