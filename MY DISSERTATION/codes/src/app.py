import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from dateutil.relativedelta import relativedelta
import warnings


from data.load_data import load_data
from utils.utils import create_dataset

# Filter out the specific FutureWarning
warnings.filterwarnings('ignore')

# Function to load the model
def load_model():
    return joblib.load("linear regression_12.joblib")

# Function to make predictions
def make_predictions(model, steps):

    monthly_data = pd.read_csv('monthly_data.csv')
    monthly_data.Date = pd.to_datetime(monthly_data.Date)

    data = []
    dates = []
    
    data = list(monthly_data.Close)
    dates = list(monthly_data.Date)
    graph_data = data.copy()
    graph_dates = dates.copy()

    for _ in range(steps):

        dataset = load_data(data,dates)[-12:]
        new_date = graph_dates[-1] + relativedelta(months=1)
        X = dataset.drop('Close', axis=1)
        y = dataset['Close']
        features = [list(y) + list(X.iloc[-1])]

        prediction = model.predict(features)[0]
        graph_data.append(prediction)
        graph_dates.append(new_date)
        data.append(prediction)
        dates.append(new_date)
        data = data[1:]
        dates = dates[1:]

    return graph_data,graph_dates

# Streamlit application
def main():
    st.title("Mutual Fund Stock Price Forecast")

    # Load the model
    model = load_model()

    # Sidebar for user input
    st.sidebar.title("Settings")
    steps = st.sidebar.slider("Select number of steps to forecast", min_value=1, max_value=100, value=10)

    # Forecast and plot
    if st.sidebar.button("Forecast"):
        graph_data,graph_dates = make_predictions(model, steps)
        df = pd.DataFrame({'Value': graph_data}, index=graph_dates)
        st.line_chart(df, use_container_width=True)      
        st.write(f"Forecast Values:{graph_data[-1]}")

if __name__ == "__main__":
    main()
