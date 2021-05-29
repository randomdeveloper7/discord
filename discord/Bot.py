import discord
import random

from discord.ext import commands
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    channel = client.get_channel(847753042753617990)
    await channel.send('This is a test server for testing bots')

@client.command()
async def ping(ctx):
    await ctx.send(f'ping : {round(client.latency * 1000)}')

@client.command()
async def motivate(ctx, *, question):
    responses = ['We are awesome', 'Nammale kond pattum'
                'There is always light at the end of the tunnel',
                'Olam boys verum poli aada', 'Hardwork forever pays', 
                'Work hard, play hard']
    await ctx.send(f'{random.choice(responses)}')

client.run('ODQ3NjkxOTQ2NzAxMjI1OTg0.YLBwpQ.kZsN_sNUUeAz9f57FbJaV8yaWZY')
