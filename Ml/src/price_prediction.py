import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import logging

# Create a logger object.
logger = logging.getLogger('my_logger')

# Set the level of the logger. This can be DEBUG, INFO, ERROR, etc.
logger.setLevel(logging.DEBUG)

# Create a file handler for outputting log messages to a file
log_handler = logging.FileHandler('my_logs.log')

# Format the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(log_handler)

def predict_price(file_path, rooms, area):
    with open(file_path, 'r') as f:
        data = json.load(f)
    logger.info("File read correctly")
    df = pd.DataFrame.from_dict(data, orient='index')

    print(df)
    df['price'] = df['price'].str.replace('zl', '').str.replace(' ', '')

    for index, row in df.iterrows():
        try:
            pd.to_numeric(row['price'])
        except:
            df.drop(index, inplace=True)

    df['price'] = df['price'].astype(int)
    # Attempt to convert values in 'area' column to float, replacing non-numeric values with NaN
    df['area'] = pd.to_numeric(df['area'].str.replace('m2', '').str.replace(',', '.'), errors='coerce')

    # Remove rows in the dataframe where NaN values exist
    df = df.dropna(subset=['area'])
    df['rooms_amount'] = pd.to_numeric(df['rooms_amount'])

    df = df[['price', 'area', 'rooms_amount']]
    logger.info("Data frame created")
    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean squared error: {mse:.2f}")
    logger.info("Calculations finished")
    input_data = [[area, rooms]]
    predicted_price = model.predict(input_data)[0]
    print(f"W FUNKCJI PREDICTED: {predicted_price}")
    return predicted_price