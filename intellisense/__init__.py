def build_prefix_tree():
    # Use notebook code
    pass


# Build prefix tree based knowledge base
build_prefix_tree()


def suggest_via_prefix_tree(word):
    if word is None or word == '':
        return list()

    return ['X', 'Y', 'Z']


def suggest_via_model(word):
    raise NotImplementedError('Not implemented yet for AI strategy')
