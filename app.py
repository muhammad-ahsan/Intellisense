import connexion
from connexion import RestyResolver
from flask import render_template

options = {"swagger_ui": True,
           'swagger_url': '/'}

connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
app = connexion_app.app
connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@app.route('/io')
def io_html():
    return render_template('io.html')


if __name__ == '__main__':
    app.run(port=5000)
