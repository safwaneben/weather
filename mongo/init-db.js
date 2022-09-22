db = db.getSiblingDB("weather_db");
db.weather_tb.drop();

db.weather_tb.insertMany([
    {
        "id": 1,
        "ville": "Nice",
        "temperature": 30,
        "date":"2019-09-07 08:14"
    },
    {
        "id": 2,
        "ville": "Monaco",
        "temperature": 13,
        "date":"2020-09-07 05:04"
    },
    {
        "id": 3,
        "ville": "Monaco",
        "temperature": 13,
        "date":"2021-09-07 11:31"
    },
]);
