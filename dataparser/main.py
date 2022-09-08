from flask import Flask
import requests


app = Flask(__name__)


@app.route("/data_parser")
def data_parser():
    return "<p><strong>Je suis le data parser service</strong></p>"


HOST = '0.0.0.0'
PORT = 8082


if __name__ == '__main__':

    app.run(host=HOST,
            debug=False,  # automatic reloading enabled
            port=PORT)