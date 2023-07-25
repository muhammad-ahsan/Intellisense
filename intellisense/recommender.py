from abc import ABCMeta
from abc import abstractmethod
from typing import Dict, Set

from phonetisch.algorithms import Soundex

soundex = Soundex()


class IRecommender(metaclass=ABCMeta):
    @staticmethod
    def post_process_recommendations(recommendations: Dict[str, float]) -> Dict[str, float]:
        return recommendations

    @abstractmethod
    def get_recommendations(self, *args) -> Dict[str, float]:
        """ Retrieve recommendations as dictionary
        """

    @abstractmethod
    def _build_recommendations(self, *args) -> Dict[str, float]:
        """" Build recommendations
        """


class PhoneticRecommender(IRecommender):

    def __init__(self, vocabulary: Set[str]):
        self.recommendations_idx: Dict[str, set[str]] = self._build_recommendations(vocabulary)

    def get_recommendations(self, word: str) -> Dict[str, float]:
        if word is None or word == '':
            return {}
        code = soundex.encode_word(word)
        recommendations = self.recommendations_idx[code] if code in self.recommendations_idx.keys() else []
        weight = [1.0 for i in range(len(recommendations))]
        return self.post_process_recommendations(dict(zip(recommendations, weight)))

    def _build_recommendations(self, vocabulary: set) -> Dict[str, Set[str]]:
        idx = dict()
        for value_word in vocabulary:
            key: str = soundex.encode_word(value_word)
            if key in idx.keys():
                idx[key].add(value_word)
            else:
                idx[key] = set()
                idx[key].add(value_word)
        return idx
