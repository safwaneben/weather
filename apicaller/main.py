from crypt import methods
from types import MethodType
from flask import Flask, jsonify, request
import requests
import pymongo
from pymongo import MongoClient


#client = MongoClient('mongo', 27017, username='root', password='example')

app = Flask(__name__)

def get_db():
    print('Getting DB ...')
    client = MongoClient(host='test_mongodb',
                        port=27017, 
                        username='root', 
                        password='example',
                        authSource='admin')
    print('client = ', client)
    db = client['weather_db']
    return db

@app.route('/')
def ping_server():
    return 'Welcome to the Anas\'s & Safwan\'s API Weather caller !'

@app.route('/all')
def get_stored_weather():
    db = get_db()
    _weathers = db.weather_tb.find()
    weathers = [{"id": weather["id"], "ville": weather["ville"], "temperature": weather["temperature"], "date": weather["date"]} for weather in _weathers]
    return jsonify({"weathers": weathers})


# Example : curl -H "Content-Type: application/json" -X POST -d {\"ville\":\"Antibes\",\"temperature\":18,\"date\":\"2021\-09\-09\ 09:22\"} http://172.23.0.6:8080/add
@app.route('/add', methods=['POST'])
def add_weather():
    req = request.json
    weather={
        "id": 4,
        "ville": req["ville"],
        "temperature": req["temperature"],
        "date":req["date"]
    }
    db = get_db()
    db.weather_tb.insert_one(weather)
    return "ok"



@app.route("/apicaller")
def apicaller():


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