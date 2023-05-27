from data_collection import fetch_data
from data_processing import process_data
from machine_learning import train_model
from presentation import print_predictions

data = fetch_data()
if data is not None:
    df = process_data(data)
    model = train_model(df)
    # Replace 'current_price' with your actual target variable
    print_predictions(model, df.drop('current_price', axis=1))
else:
    print("Failed to fetch data")
