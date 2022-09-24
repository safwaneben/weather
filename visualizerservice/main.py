from flask import Flask, render_template
import requests
import os
import plotly.graph_objects as go
import plotly
import json

app = Flask(__name__)


@app.route("/visualizer")
def visualizer():
    FORECAST_HORIZON=10
    response = requests.get('https://predictionsaf.herokuapp.com/prediction')

    fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
    fig.add_trace(go.Scatter(
        x=[i for i in range(FORECAST_HORIZON)],
        y=response.json()["predictions"],
        name="Predictions"
    ))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Predictions"
    return render_template('pred.html', graphJSON=graphJSON, header=header)


HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 8084)

if __name__ == '__main__':

    app.run(host=HOST,
            debug=True,
            port=PORT)