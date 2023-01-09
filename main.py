import nextcord
from nextcord.ext import commands
import threading
from datetime import datetime
from datetime import timezone
import os

activity = nextcord.Activity(name='Paragon Studios', type=nextcord.ActivityType.watching)
bot = commands.Bot(activity=activity)

def UTC_datetime_to_timestamp(time):
    return time.replace(tzinfo=timezone.utc).timestamp()

async def find_channel_by_name(name,category):
    for channel in category.text_channels:
        if channel.name.lower() == name.lower():
            return channel
    return None

class MainStuff(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @bot.event
    async def on_ready():
        print(f'Connected to discord w/ username: {bot.user}')

    @bot.slash_command(description="Pong")
    async def ping(self, interaction: nextcord.Interaction):
        created_at = interaction.created_at
        new_msg = await interaction.send(content="Pong!")
        created_at_msg = await new_msg.fetch()
        await new_msg.edit(content=f"Pong! {round((created_at_msg.created_at.timestamp()-created_at.timestamp())*1000)}ms")

class TicketSystem(commands.Cog):
    def __init__(self,bot):
            self.bot = bot
    @bot.slash_command(description="Creates a report ticket. Please see <#1047503210769809458> .")
    async def create_ticket(self, interaction: nextcord.Interaction):
        msg_creating = await interaction.send(ephemeral=True,content="Creating Ticket...")
        ref_channel = await bot.fetch_channel("1047503210769809458")
        if await find_channel_by_name(f"ticket-{interaction.user.id}",ref_channel.category) == None:
            report_format_channel = await bot.fetch_channel("1047503210769809458")
            ticket_channel = await report_format_channel.category.create_text_channel(f"ticket-{interaction.user.id}")    
            await ticket_channel.send(content=f"<@{interaction.user.id}>\nhttps://nohello.net/ \nExplain your problem, is this a exploiter alert, or a personal conflict with a staff member?\n\n`/remove_ticket`")
            await msg_creating.edit(content=f"<#{ticket_channel.id}>")
        else:
            await msg_creating.edit(content=f"You already have a ticket channel!")


    @bot.slash_command(description="Removes a report ticket.")
    async def remove_ticket(self, interaction: nextcord.Interaction):
        msg_removing = await interaction.send(ephemeral=True,content="Removing Ticket...")
        ref_channel = await bot.fetch_channel("1047503210769809458")
        currentchannel = await find_channel_by_name(f"ticket-{interaction.user.id}", ref_channel.category)
        if currentchannel == interaction.channel:
            await currentchannel.delete()
        else:
            await msg_removing.edit(content=f"This is not your channel!")

class HelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    bot_slash_commands_for_help_command = [
        ["create_ticket", "Creates a report ticket. Please see <#1047503210769809458>."],
        ["remove_ticket", "Removes a report ticket."],
        ["help", "Shows this, 'See a list of commands'"],
    ]

    bot_slash_commands_for_help_command_but_a_string = ""

    for command in bot_slash_commands_for_help_command:
        bot_slash_commands_for_help_command_but_a_string = bot_slash_commands_for_help_command_but_a_string + f"`{command[0]}`: **{command[1]}**\n"

    @bot.slash_command(description="See a list of commands")
    async def help(self, interaction: nextcord.Interaction):
        global bot_slash_commands_for_help_command_but_a_string
        await interaction.send(ephemeral=True,content=bot_slash_commands_for_help_command_but_a_string)

class Misc(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @bot.slash_command(description="YOU DO NOT NEED TO SEND AN EXAMPLE")
    async def no_examples(self, interaction: nextcord.Interaction):
        await interaction.send(content="**YOU DO NOT NEED TO SEND AN EXAMPLE!!**")

    @bot.slash_command(description="Info about server")
    async def serverinfo(self, interaction: nextcord.Interaction):
        guild = interaction.guild
        await interaction.send(ephemeral=True, content=f"""```yml
    OWNER: {guild.owner_id}

    SERVER MEMBER COUNT: {guild.member_count}
    BOTS: {len(guild.bots)}

    TEXT CHANNEL COUNT: {len(guild.text_channels)}
    VOICE CHANNEL COUNT: {len(guild.voice_channels)}

    ROLES: {len(guild.roles)}
    EMOJIS: {len(guild.emojis)}
    ```""")

bot.add_cog(MainStuff(bot))
bot.add_cog(TicketSystem(bot))
bot.add_cog(HelpCommand(bot))
bot.add_cog(Misc(bot))

def start_server():
    os.system("gunicorn -w 4 'app:app'")
threading.Thread(target=start_server).start()

bot.run(os.environ.get("TOKEN"))