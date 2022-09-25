from flask import Flask, jsonify, request
import requests
import psycopg2
import json

from flask import Flask
import os


#client = MongoClient('mongo', 27017, username='root', password='example')

app = Flask(__name__)
#DATABASE_URL = os.environ['DATABASE_URL']


@app.route('/')
def ping_server():
    return 'Welcome to the Anas\'s & Safwane\'s API Weather caller !'

@app.route('/all')
def get_stored_weather():
    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn = psycopg2.connect(
    host="ec2-3-219-19-205.compute-1.amazonaws.com",
    database="d2nqci8r1mchg9",
    user="gsjgnzydmirpnp",
    password="0c1ce057df7dc7bbdf815ce346848affe0daea955575be77ad011a9f2b59330a")
    
    curr = conn.cursor()
    curr.execute("select * from weather")
    res = json.dumps(curr.fetchall())
    conn.close()
    return res


# Example : curl -H "Content-Type: application/json" -X POST -d {\"ville\":\"Antibes\",\"temperature\":18,\"date\":\"2021\-09\-09\ 09:22\"} http://172.23.0.6:8080/add
@app.route('/add')
def add_weather():
    req = apicaller()
    print(req)
    weather={
        "date":req["date"],
        "ville": req["ville"],
        "temperature": req["temperature"]
    }

    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    
    conn = psycopg2.connect(
    host="ec2-3-219-19-205.compute-1.amazonaws.com",
    database="d2nqci8r1mchg9",
    user="gsjgnzydmirpnp",
    password="0c1ce057df7dc7bbdf815ce346848affe0daea955575be77ad011a9f2b59330a")
    
    curr = conn.cursor()

    
    curr.execute("INSERT INTO weather VALUES("+"\'"+weather['date']+"\',\'"+
    weather['ville']+"\',\'"+str(weather['temperature'])+"\')")
  
    # COMMIT THE ABOVE REQUESTS
    conn.commit()

    conn.close()
    
    return "ok"

def apicaller():

    params = {
    'access_key': '0d04d9264a63b76659c58596c16e0fda',
    'query': 'Nice'
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    res = {
        "date":api_response['location']['localtime'],
        "ville":api_response['location']['name'],
        "temperature":api_response['current']['temperature']
    }
    return res


HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 8080)

if __name__ == '__main__':

    app.run(host=HOST,
            debug=True,
            port=PORT)