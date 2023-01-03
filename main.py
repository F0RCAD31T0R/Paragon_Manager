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


def start_server():
    import status
    reload(status)

threading.Thread(target=start_server).start()

bot.run(os.environ.get("TOKEN"))