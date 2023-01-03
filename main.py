import nextcord
from nextcord.ext import commands
import threading
import os

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Connected to discord w/ username: {bot.user}')

@bot.slash_command(description="Pong")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!")

@bot.slash_command(description="Creates a report ticket. Please see <#1047503210769809458> .")
async def create_ticket(interaction: nextcord.Interaction):
    interaction.send(ephemeral=True,content="Creating Ticket...")
    ticket_channel = await bot.fetch_channel("1047503210769809458").category.create_text_channel(f"ticket-{interaction.user.id}")    
    await ticket_channel.send(content=f"<@{interaction.user.id}>\nhttps://nohello.net/ \nExplain your problem, is this a exploiter alert, or a personal conflict with a staff member?")
#from markupsafe import escape
#from flask import Flask
#
#app = Flask(__name__)
#
#@app.route('/status/')
#def status():
#    #f = open("./html/status/offline.html")
#    #e = f.read()
#    #f.close()
#    return "Bot is online [The server is online, this status system doesn't work properly yet.]"
# threading.Thread(target=app.run).start()

# Have you ever seen double comments? that's how you know this code is messy.

bot.run(os.environ.get("TOKEN"))