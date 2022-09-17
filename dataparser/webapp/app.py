from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from dataparser !'


@app.route("/data_parser")
def data_parser():
    return "<p><strong>Je suis le data parser service</strong></p>"

PORT=int(os.environ.get('PORT', 8082))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
