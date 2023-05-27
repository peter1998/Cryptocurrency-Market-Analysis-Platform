import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def process_data(data):
    df = pd.DataFrame(data)
    # Convert numerical columns to numeric type
    numerical_columns = ['current_price', 'market_cap', 'total_volume']
    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # Exclude 'id' column from the dataset
    df = df[numerical_columns]

    return df


def train_model(df):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(
        'current_price', axis=1), df['current_price'], test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model


# Example data
data = [{'id': 'bitcoin', 'current_price': 50000, 'market_cap': 1000000000, 'total_volume': 50000000},
        {'id': 'ethereum', 'current_price': 2000, 'market_cap': 500000000, 'total_volume': 20000000}]

df = process_data(data)
model = train_model(df)
