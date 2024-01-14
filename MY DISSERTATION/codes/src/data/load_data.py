import yfinance as  yf
import pandas as pd
import os
from icecream import ic

from utils.utils import (
    calculate_rolling_average,
    calculate_volatility
)

def load_data(close_prices:list[float], dates:list):

    monthly_data = pd.DataFrame({
        'Close': close_prices
    })
    monthly_data.index = dates

    # # Calculating Percentage Increase from Previous Close
    # monthly_data['previous_close'] = monthly_data['Close'].shift(1)
    # monthly_data.dropna(inplace=True)
    # monthly_data['percentage_increase_from_previous_close'] = (monthly_data['Close'] - monthly_data['previous_close'])/monthly_data['previous_close']*100
    # monthly_data.drop('previous_close', axis=1, inplace=True)

    # Calculating Multiple Rolling Averages for Monthly Data
    monthly_data['3_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,3)
    monthly_data['6_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,6)
    monthly_data['9_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,9)
    monthly_data['12_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,12)
    # monthly_data['24_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,24)
    # monthly_data['36_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,36)

    # Calculating Multiple Rolling Volatilities for Monthly Data
    monthly_data['3_month_volatility'] = calculate_volatility(monthly_data.Close,3)
    monthly_data['6_month_volatility'] = calculate_volatility(monthly_data.Close,6)
    monthly_data['9_month_volatility'] = calculate_volatility(monthly_data.Close,9)
    monthly_data['12_month_volatility'] = calculate_volatility(monthly_data.Close,12)

    return monthly_data



    


# def load_data():

#     path = os.path.join(
#         os.getcwd(),
#         "data",
#         "Us Inflation rate.xlsx"
#     )
#     ic(path)

#     inflation_data = pd.read_excel(path)

#     # Melt the dataframe to convert month columns into rows
#     inflation_melted = inflation_data.melt(id_vars=["Year"], var_name="Month", value_name="Inflation Rate")

#     # Remove rows with 'Ave' in Month column and any rows with NaN in 'Year' or 'Inflation Rate'
#     inflation_melted = inflation_melted[inflation_melted['Month'] != 'Ave']
#     inflation_melted = inflation_melted.dropna(subset=['Year', 'Inflation Rate'])

#     # Convert 'Year' and 'Month' into a datetime index (last day of each month)
#     inflation_melted['Date'] = pd.to_datetime(inflation_melted['Year'].astype(int).astype(str) + '-' + inflation_melted['Month'] + '-1')
#     inflation_melted['Date'] = inflation_melted['Date'] + pd.offsets.MonthEnd(0)

#     # Set the 'Date' column as the index and drop unnecessary columns
#     inflation_melted = inflation_melted.set_index('Date')
#     inflation_melted = inflation_melted.drop(columns=['Year', 'Month'])

#     # Sort the data by date
#     inflation_melted = inflation_melted.sort_index()

#     # Display the first few rows of the transformed data
#     inflation_melted.head()

#     # Set a mutual fund using ticker symbol
#     ticker_symbol = "VFINX"

#     # Fetch mutual fund data
#     mutual_fund = yf.Ticker(ticker_symbol)
#     # Get past data of 15yrs
#     history = mutual_fund.history(period='1y')

#     #  Data in tabular format
#     data = pd.DataFrame(history)

#     # Make index dtype to date-time
#     data.index = pd.to_datetime(data.index)

#     # Daily close data
#     daily_data = data[['Close']]

#     # Resample the data to monthly frequency and take the last value of each month
#     monthly_data = daily_data.resample('M').last()

#     # Calculating Percentage Increase from Previous Close
#     monthly_data['previous_close'] = monthly_data['Close'].shift(1)
#     monthly_data.dropna(inplace=True)
#     monthly_data['percentage_increase_from_previous_close'] = (monthly_data['Close'] - monthly_data['previous_close'])/monthly_data['previous_close']*100

#     # Calculating Multiple Rolling Averages for Monthly Data
#     monthly_data['3_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,3)
#     monthly_data['6_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,6)
#     monthly_data['9_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,9)
#     monthly_data['12_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,12)
#     # monthly_data['24_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,24)
#     # monthly_data['36_month_rolling_avg'] = calculate_rolling_average(monthly_data.Close,36)

#     # Calculating Multiple Rolling Volatilities for Monthly Data
#     monthly_data['3_month_volatility'] = calculate_volatility(monthly_data.Close,3)
#     monthly_data['6_month_volatility'] = calculate_volatility(monthly_data.Close,6)
#     monthly_data['9_month_volatility'] = calculate_volatility(monthly_data.Close,9)
#     monthly_data['12_month_volatility'] = calculate_volatility(monthly_data.Close,12)
#     # monthly_data['24_month_volatility'] = calculate_volatility(monthly_data.Close,24)
#     # monthly_data['36_month_volatility'] = calculate_volatility(monthly_data.Close,36)

#     monthly_data.index = monthly_data.index.strftime('%b-%Y')
#     inflation_melted.index = inflation_melted.index.strftime('%b-%Y')
    
#     return monthly_data.merge(inflation_melted, how='left', left_index=True, right_index=True)