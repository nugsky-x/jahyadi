import discord
import json
import pprint
from os import environ

client = discord.Client()
gamesMap = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.lower() == 'p':
        await message.channel.send('Apa kau ga malu, salam pakai P?')


client.run(environ.get('BOT_TOKEN'))