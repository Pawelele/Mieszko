import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def predict_price(file_path, rooms, area):
    with open(file_path, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame.from_dict(data, orient='index')
    df['price'] = df['price'].str.replace('zl', '').str.replace(' ', '')

    for index, row in df.iterrows():
        try:
            pd.to_numeric(row['price'])
        except:
            df.drop(index, inplace=True)

    df['price'] = df['price'].astype(int)
    df['area'] = df['area'].str.replace('m2', '').str.replace(',', '.').astype(float)
    df['rooms_amount'] = pd.to_numeric(df['rooms_amount'])

    df = df[['price', 'area', 'rooms_amount']]

    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean squared error: {mse:.2f}")

    input_data = [[area, rooms]]
    predicted_price = model.predict(input_data)[0]
    return predicted_price