from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

def getapp():
    return app

app.run()