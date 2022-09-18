from flask import Flask, jsonify
import requests
from pymongo import MongoClient


#client = MongoClient('mongo', 27017, username='root', password='example')

app = Flask(__name__)


def get_db():
    print('Getting DB ...')
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='example',
                        authSource="admin")
    print('client = ', client)
    db = client["weather_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        print('db = ', db)
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})

    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()


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