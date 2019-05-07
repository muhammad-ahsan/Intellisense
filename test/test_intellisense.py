def test_prefix_tree(my_prefix_tree):
    assert len(my_prefix_tree.recommend('')) == 0
