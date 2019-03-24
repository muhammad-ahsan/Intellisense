from intellisense import suggest_via_prefix_tree


def test_prefix_get_next_word():
    assert len(suggest_via_prefix_tree('')) == 0
