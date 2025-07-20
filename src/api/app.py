from fastapi import FastAPI
from src.api.routes.price import price_router

app = FastAPI()

app.include_router(price_router)
