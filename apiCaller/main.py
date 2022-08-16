from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><strong>Hello, World!</strong></p>"

if __name__ == '__main__':

    app.run()