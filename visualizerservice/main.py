from flask import Flask
import requests

app = Flask(__name__)


@app.route("/visualizer")
def visualizer():
    return "<p><strong>Je suis le visualizer</strong></p>"

HOST = '0.0.0.0'

if __name__ == '__main__':

    app.run(host=HOST)