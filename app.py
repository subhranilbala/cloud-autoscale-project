from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "App running on VM"

@app.route('/load')
def load():
    # simulate CPU load
    for i in range(10**7):
        pass
    return "Load generated"

app.run(host='0.0.0.0', port=5000)
