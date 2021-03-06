import uuid

from flask import jsonify, request

from intellisense import algorithms
from intellisense import helper

# How to create these objects Lazily?
prefix_tree = algorithms.PrefixTree(helper.get_vocabulary("en"))
phonetic_index = algorithms.PhoneticIndex(helper.get_vocabulary("en"))


def health_check():
    """Response handler to api call"""
    print(get_recommendations("massachusetts"))
    return jsonify({'id': uuid.uuid1(), 'message': 'HURRAH! the service is healthy'})


def response():
    """Response handler to api call"""
    keyword = request.args.get('keyword')
    return get_recommendations(keyword)


def get_recommendations(keyword: str):
    """List of dictionaries recommendation from algorithmic strategies bases on arguments"""
    recommendations = {"model_1": prefix_tree.recommend(keyword),
                       "model_2": phonetic_index.recommend(keyword)}
    return jsonify({'id': uuid.uuid1(), 'dict': recommendations})
