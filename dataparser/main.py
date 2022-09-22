from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route("/data_parser")
def data_parser():
    return "<p><strong>Je suis le data parser service</strong></p>"


HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 8082)


if __name__ == '__main__':

    app.run(host=HOST,
            debug=True,
            port=PORT)