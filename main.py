from fastapi import FastAPI
from api.predict import router

app = FastAPI(
    title="Sales Forecasting API",
    description="Forecast next 8 weeks sales",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Sales Forecasting API is Running Successfully"
    }