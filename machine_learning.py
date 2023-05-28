from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


def train_and_predict(df):
    target_variable = 'current_price'
    X = df.select_dtypes(include=[np.number]).drop(
        target_variable, axis=1)  # Only include numeric columns
    y = df[target_variable]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return y_test, predictions
