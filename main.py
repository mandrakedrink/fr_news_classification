import pickle
import re

from fastapi import FastAPI
from models.french_article import FrenchArticle
import models.ml.classifier as clf
from config import Config

app = FastAPI(title="News Classification ML API", description="API for french news dataset ml model", version="1.0")

@app.on_event('startup')
def load_model():
    clf.tfidf = pickle.load(open(Config.tfidf_pipeline, 'rb'))
    clf.model = pickle.load(open(Config.model, 'rb'))


@app.post('/predict', tags=["predictions"])
async def get_prediction(french_article: FrenchArticle):

    text = french_article.data[0]
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)

    features = clf.tfidf.transform([text])
    prediction = clf.model.predict(features).tolist()
    prediction = Config.id_to_category[prediction[0]]
    log_proba = clf.model.predict_proba(features).tolist()[0]
    print(log_proba, len(log_proba), log_proba)
    log_proba = {Config.id_to_category[i]: prob for i, prob in enumerate(log_proba)}
    return {"prediction": prediction,
            "log_proba": log_proba}

