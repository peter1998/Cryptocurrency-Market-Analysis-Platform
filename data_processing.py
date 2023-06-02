import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy import stats


def process_data(data):
    df = pd.DataFrame(data)
    # Convert numerical columns to numeric type
    numerical_columns = ['current_price', 'market_cap', 'total_volume']
    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # Exclude 'id' column from the dataset
    df = df[numerical_columns]

    # Check for missing values in the DataFrame
    missing_values = df.isnull()
    print("Missing values in each column:\n", missing_values.sum())

    # Fill missing values with a default value
    df_filled = df.fillna(0)
    print("Data after filling missing values:\n", df_filled.head())

    # Alternatively, drop rows with missing values
    df_dropped_rows = df.dropna()
    print("Data after dropping rows with missing values:\n", df_dropped_rows.head())

    # Check for missing values in the filled DataFrame
    missing_values_filled = df_filled.isnull().sum()
    print("Missing values in each column after filling:\n", missing_values_filled)

    # Detect outliers using Z-score
    z_scores = np.abs(stats.zscore(df_filled))
    outliers = np.where(z_scores > 2.5)
    print("Outliers detected at indices:\n", outliers)

    # Remove outliers
    df_no_outliers = df_filled[(z_scores < 2.5).all(axis=1)]
    print("Data after removing outliers:\n", df_no_outliers.head())

    # Check for inconsistencies in data types
    print("Data types in each column:\n", df_no_outliers.dtypes)

    return df_no_outliers  # return the DataFrame without outliers


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
