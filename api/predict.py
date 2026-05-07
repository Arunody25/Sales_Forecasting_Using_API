from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib

router = APIRouter()

# Load trained model
model = joblib.load("models/best_model.pkl")


# Input schema
class SalesInput(BaseModel):
    lag_1: float
    lag_7: float
    lag_30: float
    rolling_mean_7: float
    rolling_std_7: float
    day_of_week: int
    month: int
    is_holiday: int


# Prediction API
@router.post("/predict")
def predict_sales(data: SalesInput):

    input_data = pd.DataFrame([{
        "lag_1": data.lag_1,
        "lag_7": data.lag_7,
        "lag_30": data.lag_30,
        "rolling_mean_7": data.rolling_mean_7,
        "rolling_std_7": data.rolling_std_7,
        "day_of_week": data.day_of_week,
        "month": data.month,
        "is_holiday": data.is_holiday
    }])

    prediction = model.predict(input_data)

    return {
        "forecasted_sales": prediction.tolist()
    }