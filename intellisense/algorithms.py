from abc import abstractmethod

from phonetisch.algorithms import Soundex

soundex = Soundex()


class IRecommender:
    @staticmethod
    def post_process_recommendations(recommendations: dict[str, float]) -> dict[str, float]:
        return recommendations

    @abstractmethod
    def get_recommendations(self, word: str) -> dict[str, float]:
        raise NotImplementedError("Abstract method have no implementation")

    @abstractmethod
    def _build_recommendations(self, word: str) -> dict[str, float]:
        raise NotImplementedError("Abstract method have no implementation")


class PhoneticRecommender(IRecommender):

    def __init__(self, vocabulary: set[str]):
        self.phonetic_index: dict[str, set[str]] = self._build_recommendations(vocabulary)

    def get_recommendations(self, word: str) -> dict[str, float]:
        if word is None or word == '':
            return {}
        code = soundex.encode_word(word)
        recommendations = self.phonetic_index[code] if code in self.phonetic_index.keys() else []
        weight = [1.0 for i in range(len(recommendations))]
        return self.post_process_recommendations(dict(zip(recommendations, weight)))

    def _build_recommendations(self, vocabulary: set) -> dict[str, set[str]]:
        idx = dict()
        for value_word in vocabulary:
            key: str = soundex.encode_word(value_word)
            if key in idx.keys():
                idx[key].add(value_word)
            else:
                idx[key] = set()
                idx[key].add(value_word)
        return idx
