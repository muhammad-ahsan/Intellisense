import connexion
from flask import jsonify
from connexion import RestyResolver

connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app = connexion_app.app
app.url_map.strict_slashes = False
connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@app.route('/')
def index_html():
    return jsonify({'message': 'Started API successfully ...'})


if __name__ == '__main__':
    print('Welcome from AI driven intellisense')
    app.run(port=8080)
