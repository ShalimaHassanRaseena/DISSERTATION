from icecream import ic
from sklearn.metrics import (
    mean_squared_error, 
    mean_absolute_percentage_error,
    r2_score,
    mean_absolute_error
)
import matplotlib.pyplot as plt

def evaluate_forecast(model, dataset, target_column='Close', window=1, steps=1):

    X = dataset.drop(target_column, axis=1)
    indexes = X.index
    X.reset_index(drop=True,inplace=True)
    y = dataset[target_column]
    y.reset_index(drop=True,inplace=True)

    actuals = []
    predictions = []
    dates = []

    y_ = y.copy()

    for i in range(len(y) - window - 1):
        if i == 0 or i%steps == 0:
            features = list(y[i:(i + window)]) + list(X.iloc[i])
            
        else:
            features = list(y_[i:(i + window)]) + list(X.iloc[i])

        prediction = model.predict([features])[0]
        y_[i + window] = prediction
        actual = y[i + window]
        date = indexes[i + window]

        actuals.append(actual)
        predictions.append(prediction)
        dates.append(date)
    
    plt.figure()
    plt.plot(dates, actuals)
    plt.plot(dates, predictions)
    plt.show()

    ic(mean_squared_error(actuals, predictions))
    ic(mean_absolute_percentage_error(actuals, predictions))
    ic(mean_absolute_error(actuals, predictions))
    ic(r2_score(actuals, predictions))

        
