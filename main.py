import uuid

from fastapi import FastAPI
from intellisense.algorithms import PhoneticIndex
from intellisense.helper import get_vocabulary

phonetic_index = PhoneticIndex(get_vocabulary("en"))
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The api has been started. Check http://127.0.0.1:8000/docs"}


@app.get("/recommendations")
async def recommendation(keyword: str):
    return {"recommendations": phonetic_index.recommend(keyword)}


@app.get("/health")
def health_check():
    return {'id': uuid.uuid1(), 'message': 'The api is healthy'}

#
# options = {"swagger_ui": True,
#            'swagger_url': '/api'}
#
# connexion_app = connexion.FlaskApp(__name__, specification_dir='swagger/', options=options)
# app = connexion_app.app
# connexion_app.add_api('api.yaml', resolver=RestyResolver('api'))
#
#
# @app.route('/', methods=['POST', 'GET'])
# def io_html():
#     hints = []
#     if request.method == 'POST':
#         word = request.form['word']
#         hints.append(get_recommendations_list(word))
#         return render_template('io.html', hints=hints)
#     else:
#         return render_template('io.html')


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
