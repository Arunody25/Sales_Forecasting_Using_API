# Sales Forecasting Using API

## Project Overview

This project is an end-to-end Machine Learning based Sales Forecasting System developed using Python, XGBoost, and FastAPI.

The system predicts future sales using historical sales data and exposes predictions through a REST API.

The project demonstrates:

* Data preprocessing
* Feature engineering
* Time-series forecasting
* Machine Learning model training
* Model evaluation
* REST API deployment
* GitHub version control

---

# Problem Statement

The objective of this project is to forecast future sales using historical sales data.

The system:

* handles data preprocessing,
* creates forecasting features,
* trains multiple forecasting models,
* selects the best model,
* and serves predictions using FastAPI.

---

# Technologies Used

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Programming Language   |
| Pandas       | Data Processing        |
| NumPy        | Numerical Operations   |
| Scikit-learn | ML Utilities           |
| XGBoost      | Forecasting Model      |
| FastAPI      | REST API Development   |
| Uvicorn      | API Server             |
| Joblib       | Model Saving & Loading |
| Git & GitHub | Version Control        |

---

# Project Structure

```text
Sales_Forecasting_Using_API/
│
├── api/
│   └── predict.py
│
├── models/
│   └── best_model.pkl
│
├── data/
│   └── cleaned_sales_data.csv
│
├── notebooks/
│   └── End_to_End_Time_Series_Forecasting_System_with_API.ipynb
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Workflow of the Project

## 1. Data Collection

Historical sales data was collected and used for forecasting future sales.

---

## 2. Data Preprocessing

The dataset was cleaned by:

* handling missing values,
* removing duplicates,
* formatting date columns,
* sorting time-series data.

---

## 3. Feature Engineering

Time-series features were created to improve forecasting accuracy.

### Features Used

| Feature        | Description                      |
| -------------- | -------------------------------- |
| Lag_1          | Previous day sales               |
| Lag_7          | Previous week sales              |
| Lag_30         | Previous month sales             |
| Rolling_Mean_7 | 7-day rolling average            |
| Rolling_Std_7  | 7-day rolling standard deviation |
| Month          | Month number                     |
| Week           | Week number                      |

---

## 4. Model Training

Multiple forecasting models were trained and evaluated.

Models considered:

* ARIMA/SARIMA
* Prophet
* XGBoost
* LSTM

---

## 5. Model Evaluation

Models were evaluated using:

* MAE
* RMSE
* R² Score

XGBoost performed best and was selected as the final model.

---

## 6. Model Deployment

The trained XGBoost model was saved using Joblib and deployed through FastAPI.

```python
joblib.dump(model, "best_model.pkl")
```

---

# API Development

FastAPI was used to create REST API endpoints.

## Main API Features

* Load trained model
* Accept JSON input
* Predict future sales
* Return forecast response

---

# Running the Project

## Step 1 — Clone Repository

```bash
git clone https://github.com/Arunody25/Sales_Forecasting_Using_API.git
```

---

## Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## Step 4 — Open Swagger UI

Open browser:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## POST /predict

Predicts future sales based on input features.

### Sample Input

```json
{
  "Lag_1": 100,
  "Lag_7": 120,
  "Lag_30": 150,
  "Rolling_Mean_7": 130,
  "Rolling_Std_7": 15,
  "Month": 5,
  "Week": 18
}
```

---

### Sample Output

```json
{
  "forecasted_sales": [10242505]
}
```

---

# Challenges Faced

## 1. Feature Name Mismatch

The API initially failed because feature names in prediction input did not match training features.

### Solution

Feature names were aligned exactly with the training dataset.

---

## 2. Internal Server Error

The API returned a 500 Internal Server Error due to incorrect input schema.

### Solution

The request body structure and prediction dataframe were corrected.

---

# Advantages of the Project

* Automates sales forecasting
* Reduces manual effort
* Provides scalable prediction API
* Supports future deployment
* Demonstrates end-to-end ML workflow

---

# Future Improvements

Future enhancements may include:

* Streamlit dashboard
* Cloud deployment
* Database integration
* Real-time forecasting
* Advanced visualisations
* Authentication system

---

# Conclusion

This project successfully demonstrates a complete Machine Learning forecasting pipeline from data preprocessing to API deployment.

The system predicts future sales using XGBoost and exposes predictions through a FastAPI REST API.

The project reflects practical implementation of:

* machine learning,
* feature engineering,
* forecasting,
* backend API development,
* and deployment-ready architecture.

---

# Author

Arunoday Kumar

GitHub: [https://github.com/Arunody25](https://github.com/Arunody25)
