from functools import lru_cache
import joblib
from model.car import CarModel

@lru_cache
def load_model():
    model = joblib.load("models/model.pkl")
    return model

def guess_price(model, data: CarModel):
    pred = model.predict(data)
    return pred
