from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot ONLINE! [Server is online, Idk how to make health checks yet.]"

def getapp():
    return app

app.run()