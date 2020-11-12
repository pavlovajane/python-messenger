from flask import Flask
from flask import render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

import time

db = [
    {
        'text':'Hi',
        'name':'Vasya',
        'time':time.time()
    },
    {
        'text':'Hi Vasya',
        'name':'Kolya',
        'time':time.time()
    },
    {
        'text':'Howdy?',
        'name':'Vasya',
        'time':time.time()
    }
]

def show_time():
    t = time.localtime()
    local_time = time.strftime("%H:%M:%S", t)
    return local_time

@app.route("/send")
def send_message(text, name):
    db.append({
        'text': text,
        'name': name,
        'time': time.time()
    })

@app.route("/messages")
def get_messages(after):
    filtered_db = []
    for message in db:
        if message['time'] > after:
            filtered_db.append(message)
    return filtered_db

@app.route('/static/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def hello():
    return render_template('index.html')


status = {
        'status': True,
        'name': 'Hallochen',
        'time': show_time()
            }


@app.route("/stats")
def stats():
    return jsonify(status)

app.run()