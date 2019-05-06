import uuid
from flask import jsonify, request
from intellisense import prefix_tree


def health_check():
    return jsonify({'id': uuid.uuid1(), 'message': 'The service is in good health'})


def response():
    query = request.args.get('query')
    print(query)
    result = prefix_tree.recommend(query)
    return jsonify({'id': uuid.uuid1(), 'list': result})
