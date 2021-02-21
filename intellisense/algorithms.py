"""Implementation of various intellisense strategies"""

from abc import ABCMeta, abstractmethod
from typing import Dict, Set
import pytrie
from phonetisch import soundex


class RecommendationStrategy(metaclass=ABCMeta):
    """Abstract base class for recommendations """

    def __init__(self, vocabulary: set):
        self.vocabulary = vocabulary

    @abstractmethod
    def recommend(self, word: str):
        """Method to return list of recommendations """
        raise NotImplementedError('No implementation of abstract class')


class PrefixTree(RecommendationStrategy):
    """ Implementation of RecommendationStrategy based on prefix trees """

    def __init__(self, vocabulary: set):
        super().__init__(vocabulary)
        self._prefix_tree = pytrie.SortedStringTrie.fromkeys(vocabulary)

    def recommend(self, word: str) -> set:
        if word is None or word == '':
            return set()

        if self._prefix_tree is None:
            raise Exception('Prefix tree not ready')
        return set(self._prefix_tree.keys(prefix=str.lower(word)))


class PhoneticIndex(RecommendationStrategy):
    """Use the soundex library for building index for recommendations"""

    @staticmethod
    def build_index(vocabulary: set) -> Dict[str, Set[str]]:
        """Build s phonetics algorithms based index for given vocabulary"""
        idx = dict()
        for value_word in vocabulary:
            key = soundex.encode_word(value_word)
            if key in idx.keys():
                idx[key].add(value_word)
            else:
                idx[key] = set()
                idx[key].add(value_word)
        return idx

    def __init__(self, vocabulary: set):
        super().__init__(vocabulary)
        self.phonetic_index = PhoneticIndex.build_index(self.vocabulary)

    def recommend(self, word: str) -> set:
        code = soundex.encode_word(word)
        if code in self.phonetic_index.keys():
            return self.phonetic_index[code]
        return set()
