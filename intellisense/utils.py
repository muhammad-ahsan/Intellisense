import uuid
from flask import jsonify, request
from intellisense import prefix_tree


def health_check():
    return jsonify({'id': uuid.uuid1(), 'message': 'Health is good'})


def response():
    query = request.args.get('query')
    print(query)
    result = prefix_tree.recommend(query)
    print(result)
    return jsonify({'id': uuid.uuid1(), 'list': result})
