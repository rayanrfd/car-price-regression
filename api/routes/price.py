from fastapi import FastAPI, APIRouter

price_router = APIRouter()

@price_router.post("/")
