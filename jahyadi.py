import discord
import json
import pprint
import random
from os import environ

client = discord.Client()

with open('quotes.json') as json_file:
    quotes = json.load(json_file)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'p':
        await message.channel.send('Apa kau ga malu, salam pakai P?')

    if message.content.lower() == "sudah quote":
        await message.channel.send(random.choice(quotes))

client.run(environ.get('BOT_TOKEN'))