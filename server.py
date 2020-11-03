from flask import Flask
from flask import render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

import time

def current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time



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
        'time': current_time()
            }

@app.route("/stats")
def stats():
    return jsonify(status)


app.run()