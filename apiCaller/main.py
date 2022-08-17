from flask import Flask
import requests

app = Flask(__name__)


@app.route("/get_data")
def get_data():
    params = {
    'access_key': '0d04d9264a63b76659c58596c16e0fda',
    'query': 'Paris'
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return api_response['location']['name'], api_response['current']['temperature']

if __name__ == '__main__':

    app.run()