import nextcord
from nextcord.ext import commands
import threading
import os

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Connected to discord w/ username: {bot.user}')

@bot.slash_command(description="'Pong'")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!")


from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/status/')
def status():
    #f = open("./html/status/offline.html")
    #e = f.read()
    #f.close()
    return "Bot is online [The server is online, this status system doesn't work properly yet.]"

threading.Thread(target=app.run).start()

bot.run(os.environ.get("TOKEN"))