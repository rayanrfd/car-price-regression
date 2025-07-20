from fastapi import FastAPI, APIRouter
from src.api.ai.price import load_model, guess_price
from src.api.model.car import CarModel

price_router = APIRouter()

@price_router.post('/')
async def price(car_data: CarModel):
    model, preprocessor = load_model("xgb_model.json", "preprocessor.pkl")
    price = guess_price(model, preprocessor, data=car_data)
    return price
