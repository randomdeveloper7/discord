import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODQ3NjkxOTQ2NzAxMjI1OTg0.YLBwpQ.kZsN_sNUUeAz9f57FbJaV8yaWZY')

