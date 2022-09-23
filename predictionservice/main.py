from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route("/prediction")
def prediction():
    return "<p><strong>Je suis le prediction service</strong></p>"

HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 8083)

if __name__ == '__main__':

    app.run(host=HOST,
            debug=True,
            port=PORT)