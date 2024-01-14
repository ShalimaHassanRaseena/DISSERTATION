import pandas as pd
import numpy as np

def calculate_rolling_average(close_values: list[float], period: int) -> list[float]:
    """
    Calculate the rolling average of close values over a specified period.
    Adjustments are made to keep the input and output dimension same. Careful
    consideration is also given not take the current value in calculation. That is
    if the rolling of avg for ith position is calculated, then only values till i-1
    is considered.

    Parameters:
    - close_values (List[float]): List of close price values.
    - period (int): The rolling window period for calculating the average.

    Returns:
    - List[float]: List of rolling average values.
    """

    rolling_average:list[float] = []

    for i in range(len(close_values)):

      if i == 0:
        # As there are no prev values considering the same value as avg
        rolling_average.append(close_values[i])

      elif i < period:
        # If window size is less than period cal avg based on window size
        window = close_values[:i]
        average = sum(window) / len(window)
        rolling_average.append(average)

      else:
          window = close_values[i - period + 1:i]
          average = sum(window) / len(window)
          rolling_average.append(average)

    return rolling_average

def calculate_volatility(close_values: list[float], period: int) -> list[float]:
  """
  Calculate the rolling volatility of close values over a specified period.

  Parameters:
  - close_values (List[float]): List of close price values.
  - period (int): The rolling window period for calculating volatility.

  Returns:
  - List[float]: List of rolling volatility values.
  """
  volatility: list[float] = []

  for i in range(len(close_values)):
    if i == 0:
      # If there are no previous values, set volatility to 0
      volatility.append(0.0)

    elif i < period:
      # If the window size is less than the period, calculate volatility based on the window size
      window = close_values[:i]

      if len(window) == 1:
        # If there's only one value, volatility can't be calculated, so set it to 0
        volatility.append(0.0)

      else:
        # Volatility is the percentage change between the first and last value in the window
        change = (window[-1] - window[0]) / window[0]
        volatility.append(change)

    else:
      # Calculate volatility over the specified period
      window = close_values[i - period:i]
      change = (window[-1] - window[0]) / window[0]
      volatility.append(change)

  return [100*v for v in volatility]

def create_dataset(dataset: pd.DataFrame, target_column:str='Close', window_size: int = 12) -> tuple[np.ndarray, np.ndarray]:
    """
    Create a dataset for rolling window analysis.

    This function takes a time series dataset and creates a set of features and target
    variables based on the specified rolling window size.

    Parameters:
    dataset (pd.DataFrame): The input dataset, typically a time series of values.
    window_size (int): The size of the rolling window to create features.

    Returns:
    Tuple[np.ndarray, np.ndarray]: A tuple of two numpy arrays, where the first array
                                   contains the features and the second array contains
                                   the corresponding target values.
    """

    X = dataset.drop(target_column, axis=1)
    X.reset_index(drop=True,inplace=True)
    y = dataset[target_column]
    y.reset_index(drop=True,inplace=True)

    dataX, dataY = [], []

    for i in range(len(y) - window_size - 1):
        print(i)

        features = list(y[i:(i + window_size)]) + list(X.iloc[i])
        dataX.append(features)

        target = y[i + window_size]
        dataY.append(target)

    return np.array(dataX), np.array(dataY)