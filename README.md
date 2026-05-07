# Sales Forecasting Using API

## Introduction

Sales forecasting plays an important role in business decision-making because it helps companies estimate future demand and plan their operations more effectively. In this project, a machine learning-based forecasting system was developed to predict future sales using historical sales data.

The project covers the complete workflow starting from data preprocessing and feature engineering to model training and API deployment. A FastAPI backend was used to expose the prediction model through REST APIs so that predictions can be generated dynamically.

The main objective of this project was to create a practical forecasting solution that can analyse past sales behaviour and generate future sales predictions efficiently.

---

# Objective of the Project

The objective of this project is to build an end-to-end sales forecasting system using machine learning techniques. The system should be able to:

* analyse historical sales data,
* preprocess and clean the dataset,
* generate forecasting features,
* train multiple forecasting models,
* select the best-performing model,
* and provide predictions through an API.

The project also focuses on creating a production-style backend structure suitable for real-world applications.

---

# Technologies Used

| Technology   | Purpose                         |
| ------------ | ------------------------------- |
| Python       | Core programming language       |
| Pandas       | Data preprocessing and analysis |
| NumPy        | Numerical operations            |
| Scikit-learn | Model evaluation and utilities  |
| XGBoost      | Forecasting model               |
| FastAPI      | Backend API development         |
| Uvicorn      | Running API server              |
| Joblib       | Saving and loading model        |
| Git & GitHub | Version control                 |

---

# Dataset Description

The dataset contains historical sales information used for forecasting future sales values. The data was analysed and processed before training the machine learning models.

The dataset included time-series information that helped identify sales trends and patterns over time.

---

# Data Preprocessing

Data preprocessing was performed to improve the quality of the dataset before training the models.

The following preprocessing steps were applied:

* handled missing values,
* removed duplicate records,
* converted date columns into proper datetime format,
* sorted records according to time sequence,
* cleaned inconsistent values.

These steps helped improve model performance and ensured reliable forecasting.

---

# Feature Engineering

Feature engineering was one of the most important parts of the project because machine learning models cannot directly understand time-series behaviour.

Several forecasting features were created from historical sales values.

## Lag Features

Lag features were generated to provide information about previous sales patterns.

Examples:

* Lag_1 → previous day sales
* Lag_7 → sales from previous week
* Lag_30 → sales from previous month

## Rolling Features

Rolling statistics were used to capture short-term sales trends.

Examples:

* Rolling_Mean_7
* Rolling_Std_7

## Date Features

Additional date-related features were created such as:

* month,
* week,
* day-related patterns.

These engineered features helped the model learn seasonality and historical behaviour more effectively.

---

# Model Training

Different forecasting models were trained and compared during experimentation.

The models used in this project include:

* ARIMA/SARIMA
* Prophet
* XGBoost
* LSTM

Each model was evaluated using forecasting metrics to determine which model performed best on the dataset.

---

# Model Evaluation

The models were evaluated using standard regression metrics such as:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

Among all the trained models, XGBoost achieved the best performance with lower prediction error and better forecasting accuracy.

Therefore, XGBoost was selected as the final deployment model.

---

# Why XGBoost Was Selected

XGBoost was selected because it handled time-series engineered features efficiently and produced more accurate predictions compared to other models.

Some advantages of XGBoost include:

* high prediction accuracy,
* good handling of non-linear patterns,
* reduced overfitting,
* efficient performance on structured data,
* faster prediction speed.

---

# Model Saving

After training and evaluation, the final XGBoost model was saved using Joblib.

The saved model file:

best_model.pkl

Saving the model allows predictions to be generated later without retraining the model again.

---

# API Development Using FastAPI

FastAPI was used to build the backend API for the forecasting system.

The API allows users to send input values and receive predicted sales values as a response.

FastAPI was chosen because it is:

* lightweight,
* fast,
* easy to use,
* and automatically generates API documentation.

---

# API Workflow

The workflow of the API is as follows:

1. User sends input data through API request.
2. FastAPI receives the request.
3. Input values are converted into a dataframe.
4. The trained XGBoost model processes the input.
5. The model predicts future sales.
6. Prediction result is returned as JSON response.

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
│   └── forecasting_notebook.ipynb
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Explanation of Important Files

## main.py

This file is the entry point of the FastAPI application. It initialises the API server and connects API routes.

## predict.py

This file contains the prediction endpoint logic. It loads the trained model and generates predictions.

## best_model.pkl

This file stores the trained XGBoost forecasting model.

## requirements.txt

Contains all required Python libraries needed to run the project.

---

# API Testing

The API was tested using Swagger UI generated automatically by FastAPI.

Swagger URL:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This interface allows users to test API endpoints directly from the browser.

---
# Advantages of the System

* Automates sales forecasting
* Reduces manual effort
* Provides quick predictions
* Easy to scale and deploy
* Supports real-time prediction through APIs
* Demonstrates practical machine learning deployment

---

# Future Enhancements

The project can be improved further by adding:

* cloud deployment,
* Streamlit dashboard,
* database integration,
* real-time data pipeline,
* authentication system,
* advanced visualisations,
* automated retraining pipeline.

---

# Conclusion

This project successfully demonstrates an end-to-end machine learning forecasting pipeline using XGBoost and FastAPI.

The system performs data preprocessing, feature engineering, model training, evaluation, and deployment through a REST API.

The project reflects practical implementation of forecasting techniques along with backend API development and production-style project structuring.

It also provides hands-on experience with machine learning deployment and real-world forecasting workflows.

---

# Author

Arunoday Kumar

GitHub: [https://github.com/Arunody25](https://github.com/Arunody25)
