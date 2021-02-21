"""API call handler module"""
import uuid
from flask import jsonify, request
from intellisense import algorithms
from intellisense import helper

prefix_tree = algorithms.PrefixTree(helper.get_vocabulary("en"))
phonetic_index = algorithms.PhoneticIndex(helper.get_vocabulary("en"))


def health_check():
    """Checking health of api"""
    return jsonify({'id': uuid.uuid1(), 'message': 'The service is in good health'})


def response():
    """Returning response to api call"""
    query = request.args.get('query')
    result = set()
    result = result.union(prefix_tree.recommend(query)).union(phonetic_index.recommend(query))
    return jsonify({'id': uuid.uuid1(), 'list': result})
