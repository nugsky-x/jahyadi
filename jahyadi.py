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

    if message.content.lower() == "sudah penis":
        i = random.randint(0,10)
        penis_size = "8" + ("=" * i) + "D"
        embedVar = discord.Embed(title="Peepee size machine", description="{}'s penis\n{}".format(message.author.name, penis_size), color=0x00ff00)
        await message.channel.send(embed=embedVar)
        if (i == 0):
            await message.channel.send('Apa kau ga malu, punya penis 8D?')

client.run(environ.get('BOT_TOKEN'))