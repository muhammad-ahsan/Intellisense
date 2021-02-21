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
    keyword = request.args.get('keyword')
    bucket = set()
    result = list(bucket.union(prefix_tree.recommend(keyword)).
                  union(phonetic_index.recommend(keyword)))
    return jsonify({'id': uuid.uuid1(), 'list': result})
