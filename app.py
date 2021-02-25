import connexion
from connexion import RestyResolver
from flask import jsonify

options = {"swagger_ui": True}
connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
app = connexion_app.app
connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@app.route('/')
def index_html():
    return jsonify({'message': 'Started API successfully ...'})


if __name__ == '__main__':
    print('Welcome from AI driven intellisense')
    app.run(port=5000)
