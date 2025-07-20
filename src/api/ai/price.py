from functools import lru_cache
from pathlib import Path
import joblib
import pandas as pd
from xgboost import XGBRegressor
from src.api.model.car import CarModel

@lru_cache
def load_model(model_name, preprocessor_name, path="../ml-pipeline/models/"):
    model = XGBRegressor()
    model.load_model(str(Path(path).resolve() / model_name))
    preprocessor = joblib.load(str(Path(path).resolve() / preprocessor_name))
    return model, preprocessor

def guess_price(model, preprocessor, data: CarModel):
    data = pd.DataFrame([data.model_dump()])
    data = preprocessor.transform(data)
    pred = model.predict(data)
    return float(pred[0])
