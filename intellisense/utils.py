import uuid

from flask import jsonify, request

from intellisense import algorithms
from intellisense import helper

# How to create these objects Lazily?
prefix_tree = algorithms.PrefixTree(helper.get_vocabulary("en"))
phonetic_index = algorithms.PhoneticIndex(helper.get_vocabulary("en"))


def health_check():
    """Response handler to api call"""
    print(get_recommendations_json("massachusetts"))
    return jsonify({'id': uuid.uuid1(), 'message': 'HURRAH! the service is healthy'})


def response():
    """Response handler to api call"""
    keyword = request.args.get('keyword')
    return get_recommendations_json(keyword)


def get_recommendations_list(keyword: str) -> list:
    hint_1 = list(prefix_tree.recommend(keyword).keys())
    hint_2 = list(phonetic_index.recommend(keyword).keys())
    return set(hint_1 + hint_2)


def get_recommendations_json(keyword: str):
    """List of dictionaries recommendation from algorithmic strategies bases on arguments"""
    hints = {"model_1": prefix_tree.recommend(keyword),
             "model_2": phonetic_index.recommend(keyword)}
    return jsonify({'id': uuid.uuid1(), 'dict': hints})
