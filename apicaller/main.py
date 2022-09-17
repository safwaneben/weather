from flask import Flask
import requests
import json
from flask_pymongo import PyMongo


#client = MongoClient('mongo', 27017, username='root', password='example')

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://root:example@mongo:27017/"
mongo = PyMongo(app)

@app.route("/apicaller")
def apicaller():

    print('mongo = ', mongo)

    params = {
    'access_key': '0d04d9264a63b76659c58596c16e0fda',
    'query': 'Paris'
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    res = {
        "Ville":api_response['location']['name'],
        "Temperature":api_response['current']['temperature'],
        "Date":api_response['location']['localtime']
    }
    return res


HOST = '0.0.0.0'
PORT = 8080

if __name__ == '__main__':

    app.run(host=HOST,
            debug=False,  # automatic reloading enabled
            port=PORT)