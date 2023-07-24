import uuid

from fastapi import FastAPI
from intellisense.algorithms import PhoneticIndex
from intellisense.helper import get_vocabulary

recommender = PhoneticIndex(get_vocabulary("en"))
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The api has been started. Check http://127.0.0.1:8000/docs"}


@app.get("/recommendations")
async def recommendation(keyword: str):
    return {"recommendations": recommender.get_recommendations(keyword)}


@app.get("/health")
def health_check():
    return {'id': uuid.uuid1(), 'message': 'The api is healthy'}

