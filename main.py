from data_collection import fetch_data
from data_processing import process_data
from machine_learning import train_and_predict

data = fetch_data()
if data is not None:
    df = process_data(data)
    print("df.head: ", df.head())
    y_test, predictions = train_and_predict(df)
    print("Actual values:\n", y_test)
    print("Predicted values:\n", predictions)
else:
    print("Failed to fetch data")
