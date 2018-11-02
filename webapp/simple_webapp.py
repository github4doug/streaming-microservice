from flask import Flask, render_template, jsonify
import datetime
import random
import os
import json

app = Flask(__name__)
app.secret_key = 'youwillneverguess'

@app.route('/')
def hello() -> str:
    return 'hello from the simple webapp'

@app.route('/data')
def getData() -> str:
    jsonData = loadData()
    return jsonData


@app.route('/visualize')
def visualize() -> 'html':
    return render_template('visualize.html',the_title='Visualize Realtime Streaming Data from Redis in-memory cache')

def loadData():
    # stubbed out TBD retrieve from redis
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    datafile = "testdata.json"
    json_url = os.path.join(SITE_ROOT, "static/data", datafile)
    data = json.load(open(json_url))
    tempMassageData(data)
    return jsonify(data)

def tempMassageData(data):
    for d in data:
        d['count'] += random.randint(0,5)

if __name__ == '__main__':
    app.run(debug=True)
