import uuid
from flask import jsonify, request
from intellisense import suggest_via_prefix_tree


def health_check():
    return jsonify({'id': uuid.uuid1(), 'message': 'Health is good'})


def response():
    query = request.args.get('query')
    print(query)
    result = suggest_via_prefix_tree(query)
    print(result)
    return jsonify({'id': uuid.uuid1(), 'list': result})
