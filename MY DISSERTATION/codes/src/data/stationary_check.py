from statsmodels.tsa.stattools import adfuller





def adfuller_test(data: list)->tuple[float,float]:

    # Performing the Augmented Dickey-Fuller test to check stationarity
    adf_test_result = adfuller(data)

    # Extracting the test statistic and p-value
    adf_statistic, p_value = adf_test_result[0], adf_test_result[1]

    return {
        'adf_statistic': adf_statistic, 
        'p_value': p_value
    }

if __name__ == "__main__":

    from data.dataloader import load_data

    vanguard_data = load_data()
    close_data = vanguard_data['Close']

    print(adfuller_test(close_data))

