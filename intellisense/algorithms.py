from abc import abstractmethod
from typing import Dict, Set

import pytrie
from phonetisch import soundex


class RecommendationStrategy:

    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    @abstractmethod
    def recommend(self, word: str) -> Dict[str, float]:  #
        raise NotImplementedError("Abstract method have no implementation")

    @staticmethod
    def recommendations_post_processing(recommendations: Dict[str, float]) -> Dict[str, float]:
        return recommendations


class PrefixTree(RecommendationStrategy):

    def __init__(self, vocabulary: set):
        super().__init__(vocabulary)
        self._prefix_tree = pytrie.SortedStringTrie.fromkeys(vocabulary)

    def recommend(self, word: str) -> Dict[str, float]:
        if word is None or word == '':
            return {}

        if self._prefix_tree is None:
            raise Exception('Prefix tree not ready')
        recommendations = self._prefix_tree.keys(prefix=str.lower(word))
        weight = [1.0 for i in range(len(recommendations))]
        return self.recommendations_post_processing(dict(zip(recommendations, weight)))


class PhoneticIndex(RecommendationStrategy):

    def __init__(self, vocabulary: set):
        super().__init__(vocabulary)
        self.phonetic_index = PhoneticIndex.build_index(self.vocabulary)

    @staticmethod
    def build_index(vocabulary: set) -> Dict[str, Set[str]]:
        idx = dict()
        for value_word in vocabulary:
            key = soundex.encode_word(value_word)
            if key in idx.keys():
                idx[key].add(value_word)
            else:
                idx[key] = set()
                idx[key].add(value_word)
        return idx

    def recommend(self, word: str) -> Dict[str, float]:
        if word is None or word == '':
            return {}
        code = soundex.encode_word(word)
        recommendations = self.phonetic_index[code] if code in self.phonetic_index.keys() else []
        weight = [1.0 for i in range(len(recommendations))]
        return self.recommendations_post_processing(dict(zip(recommendations, weight)))
