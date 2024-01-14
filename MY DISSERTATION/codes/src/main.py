from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error, 
    mean_absolute_percentage_error,
    r2_score,
    mean_absolute_error
)
from sklearn.metrics import r2_score
from icecream import ic

from data.load_data import load_data
from utils.utils import create_dataset
from evaluate.evaluate import evaluate_forecast

data = load_data()
X, y = create_dataset(data, window_size=12)

# Splitting the dataset into training and test sets
train_size = int(len(X) * 0.70)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size], X[train_size:len(X)]
y_train, y_test = y[0:train_size], y[train_size:len(y)]

# Creating and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

predictions = model.predict(X)

# Calculating the mean squared error
ic(mean_squared_error(y_train, train_predictions))
ic(mean_squared_error(y_test, test_predictions))

# Calculating the R2 score for both training and test sets
ic(r2_score(y_train, train_predictions))
ic(r2_score(y_test, test_predictions))

# Calculating the mean squared error
ic(mean_absolute_percentage_error(y_train, train_predictions))
ic(mean_absolute_percentage_error(y_test, test_predictions))

# Calculating the mean squared error
ic(mean_absolute_error(y_train, train_predictions))
ic(mean_absolute_error(y_test, test_predictions))

ic(mean_squared_error(y, predictions))
ic(mean_absolute_percentage_error(y, predictions))
ic(mean_absolute_error(y, predictions))
ic(r2_score(y, predictions))

print(" ")
evaluate_forecast(model,data,window=12,steps=12)
