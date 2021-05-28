import discord
from discord.ext import  commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

client.run('ODQ3NjkxOTQ2NzAxMjI1OTg0.YLBwpQ.-eNB8E7Mlg1eamJpctbqWtmxD9Q')