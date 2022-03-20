import connexion
from connexion import RestyResolver
from flask import request, render_template
from intellisense.utils import get_recommendations_list

options = {"swagger_ui": True,
           'swagger_url': '/api'}

connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
app = connexion_app.app
connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))


@app.route('/', methods=['POST', 'GET'])
def io_html():
    hints = []
    if request.method == 'POST':
        word = request.form['word']
        hints.append(get_recommendations_list(word))
        return render_template('io.html', hints=hints)
    else:
        return render_template('io.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
