import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from dataclasses import dataclass
from pandas import Series

def difference_series(series, interval=1):
    """
    Apply differencing to a time series.

    Parameters:
    series (pd.Series): The time series to be differenced.
    interval (int): The interval for differencing. Default is 1.

    Returns:
    pd.Series: The differenced time series.
    """
    differenced = series.diff(periods=interval)
    return differenced.dropna() 

def log_transform_series(series):
    """
    Apply log transformation to a time series to stabilize variance.

    Parameters:
    series (pd.Series): The time series to be log-transformed.

    Returns:
    pd.Series: The log-transformed time series.
    """
    # Applying natural logarithm; adding a small constant to avoid log(0)
    transformed = np.log(series + 1e-6)
    return transformed

@dataclass
class TimeSeriesDecomposition:
    trend: Series
    seasonal: Series
    residual: Series
    orginal: Series


def decompose_time_series(series, model='additive', freq=4*5*3):
    """
    Decompose a time series into its trend, seasonal, and residual components.

    Parameters:
    series (pd.Series): The time series to decompose.
    model (str): The type of decomposition model ('additive' or 'multiplicative').
    freq (int): The frequency of the time series. If None, it will be inferred.

    Returns:
    dict: A dictionary containing the trend, seasonal, and residual components.
    """
    decomposition = seasonal_decompose(series, model=model, period=freq)
    
    return TimeSeriesDecomposition(
        trend=decomposition.trend,
        seasonal=decomposition.seasonal,
        residual=decomposition.resid,
        orginal=series
    )
