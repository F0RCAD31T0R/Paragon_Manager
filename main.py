import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Connected to discord")

bot.run(open("../token.txt","r").read())