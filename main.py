import discord
import threading
import os

intents = discord.Intents.default()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Connected to discord")

def start_server():
    import status
    reload(status)

threading.Thread(target=start_server).start()

#bot.run("MTA1OTU1Nzk2NTQ2MTQ3NTM5OA.GDGTVR.UmVe0jEQmHQvrv9FSnk6e2SwfqNhVLw4BG5giM")
bot.run(os.environ.get("TOKEN"))