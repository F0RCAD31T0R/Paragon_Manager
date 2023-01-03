from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/status/')
def status():
    #f = open("./html/status/offline.html")
    #e = f.read()
    #f.close()
    return "Bot is online [The server is online, this status system doesn't work properly yet.]"