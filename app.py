from flask import Flask
import requests
import json

app = Flask(__name__)

online = open("./html/status/online.html").read()
offline = open("./html/status/offline.html").read()
home = open("./html/main/home.html").read()

@app.route('/')
def index():
    print(requests.get("https://paragon-manager-bot.onrender.com/status/").status_code)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/status/')
def status():
    return online

@app.route('/css/<p>')
def public(p):
    return open("./html/" + p + ".css", "r").read()

@app.route('/home/')
def phome():
    return home


def getapp():
    return app