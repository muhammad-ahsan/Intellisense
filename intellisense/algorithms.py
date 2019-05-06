from abc import abstractmethod, ABCMeta

import os
import pytrie


class RecommendationStrategy(metaclass=ABCMeta):

    @abstractmethod
    def recommend(self):
        raise NotImplementedError('No implementation of abstract class')


class PrefixTree(RecommendationStrategy):

    def __init__(self):
        self._repo = os.path.dirname(os.path.abspath(__file__))
        self._path = self._repo + '/data/training.txt'
        words = set()

        exists = os.path.isfile(self._path)
        if not exists:
            raise FileNotFoundError('Training do not exist')

        words = set(open(self._path).read().split())

        processed_words = map(lambda x: x.lower(), words)
        self._prefix_tree = pytrie.SortedStringTrie.fromkeys(processed_words)

    def recommend(self, word):
        if word is None or word == '':
            return list()

        if self._prefix_tree is None:
            raise Exception('Prefix tree not ready')
        return self._prefix_tree.keys(prefix=str.lower(word))

