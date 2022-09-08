from flask import Flask
import requests
import json

app = Flask(__name__)

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
PORT = 8081

if __name__ == '__main__':

    app.run(host=HOST,
            debug=False,  # automatic reloading enabled
            port=PORT)