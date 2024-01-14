import yfinance as yf
import pandas as pd
import numpy as np
from typing import Tuple

class StockData:

    def __init__(self,ticker_symbol:str="VFINX",period:str='1y') -> None:

        # Fetch mutual fund data
        mutual_fund = yf.Ticker(ticker_symbol)

        # Get past data
        self.daily_data = pd.DataFrame(
            mutual_fund.history(period=period)
        ).dropna()

        self.close_price_daily = self.daily_data.Close
        self.get_monthly_data()
    
    def get_monthly_data(self):
        self.monthly_data = self.daily_data.resample('M').last().dropna()
        self.close_price_monthly = self.monthly_data.Close


def create_dataset(dataset: np.ndarray, window_size: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create a dataset for rolling window analysis.

    This function takes a time series dataset and creates a set of features and target
    variables based on the specified rolling window size.

    Parameters:
    dataset (np.ndarray): The input dataset, typically a time series of values.
    window_size (int): The size of the rolling window to create features.

    Returns:
    Tuple[np.ndarray, np.ndarray]: A tuple of two numpy arrays, where the first array
                                   contains the features and the second array contains
                                   the corresponding target values.
    """
    dataX, dataY = [], []
    for i in range(len(dataset) - window_size - 1):
        a = dataset[i:(i + window_size)]
        # Normalize the array
        min_val = a.min()
        max_val = a.max()
        normalized_a = (a - min_val) / (max_val - min_val)
        dataX.append(normalized_a)
        dataY.append(dataset[i + window_size])
    return np.array(dataX), np.array(dataY)