from flask import Flask
import requests

import holt_winters
import numpy as np

app = Flask(__name__)

N_DATAS = 100
FORECAST_HORIZON = 10

def init_data():
    df = []
    for i in range(N_DATAS):
        df.append(np.random.randint(10,30))
    return df

def predict(df):
    model = holt_winters.HoltWinters()
    model.fit(df)
    return model.predict(FORECAST_HORIZON)[-FORECAST_HORIZON:]

@app.route("/prediction")
def prediction():
    df = init_data()
    predictions = predict(df)
    return {"predictions" : predictions}

HOST = '0.0.0.0'
PORT = 8083

if __name__ == '__main__':

    app.run(host=HOST,
            port=PORT)