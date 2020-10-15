import discord
import json
import pprint
import random
from os import environ

client = discord.Client()

qoutes = [
    "kau kurang empati",
    "high tech tai anjing",
    "aku berharap saja kau tak depresi besok",
    "seems like kau yang punya balls di sini"
]

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
        await message.channel.send(random.choice(qoutes))

client.run(environ.get('BOT_TOKEN'))