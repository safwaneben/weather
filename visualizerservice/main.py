from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route("/visualizer")
def visualizer():
    return "<p><strong>Je suis le visualizer</strong></p>"

HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 8084)

if __name__ == '__main__':

    app.run(host=HOST,
            debug=True,
            port=PORT)