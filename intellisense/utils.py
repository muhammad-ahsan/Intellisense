import uuid
from flask import jsonify


def health_check():
    return jsonify({'id': uuid.uuid1(), 'message': 'Health is good'})


def response():
    return jsonify({'id': uuid.uuid1(), 'message': 'Not configured yet'})
