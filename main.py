# main.py

from sklearn.model_selection import train_test_split
# Import fetch_current_market_data
from data_collection import fetch_current_market_data
from data_processing import process_data
from machine_learning import train_and_predict, compare_models

data = fetch_current_market_data()  # Use fetch_current_market_data
if data is not None:
    df = process_data(data)
    print("df.head: ", df.head())
    # Split the data into training and test sets
    X = df.drop('current_price', axis=1)
    y = df['current_price']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    compare_models(X_train, y_train)  # Compare models
    predictions = train_and_predict(X_train, y_train, X_test)
    print("Actual values:\n", y_test)
    print("Predicted values:\n", predictions)
else:
    print("Failed to fetch data")
