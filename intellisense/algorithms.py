from abc import abstractmethod
from typing import Dict, Set

from phonetisch.algorithms import Soundex

soundex = Soundex()


class RecommendationStrategy:

    def __init__(self, vocabulary: set):
        self.vocabulary: set = vocabulary

    @abstractmethod
    def get_recommendations(self, word: str) -> Dict[str, float]:
        raise NotImplementedError("Abstract method have no implementation")

    @staticmethod
    def process_recommendations(recommendations: Dict[str, float]) -> Dict[str, float]:
        return recommendations


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

    def get_recommendations(self, word: str) -> Dict[str, float]:
        if word is None or word == '':
            return {}
        code = soundex.encode_word(word)
        recommendations = self.phonetic_index[code] if code in self.phonetic_index.keys() else []
        weight = [1.0 for i in range(len(recommendations))]
        return self.process_recommendations(dict(zip(recommendations, weight)))
