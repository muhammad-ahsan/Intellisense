import os
import pytrie

repo = os.path.dirname(os.path.abspath(__file__))
path = repo + '/data/training.txt'


def build_prefix_tree(*args):
    words = set()
    if args is not None and len(args) != 0:
        for arg in args:
            words.add(arg)
    else:
        exists = os.path.isfile(path)
        if not exists:
            raise FileNotFoundError('Training do not exist')

        words = set(open(path).read().split())

    processed_words = map(lambda x: x.lower(), words)
    return pytrie.SortedStringTrie.fromkeys(processed_words)


prefix_tree_from_data = build_prefix_tree()


def suggest_via_prefix_tree(word, prefix_tree=None):
    if word is None or word == '':
        return list()

    if prefix_tree is None:
        return prefix_tree_from_data.keys(prefix=str.lower(word))
    else:
        return prefix_tree.keys(prefix=str.lower(word))


def suggest_via_model(word):
    if word is None or word == '':
        return list()
    raise NotImplementedError('Not implemented yet for AI strategy')
