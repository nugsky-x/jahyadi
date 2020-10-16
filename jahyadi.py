import discord
import json
from pprint import pprint
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

    elif message.content.lower() == "sudah quote":
        await message.channel.send(random.choice(quotes))

    elif message.content.lower().startswith("sudah penis"):
        await client.wait_until_ready()
        i = random.randint(0,10)
        penis_size = "8" + ("=" * i) + "D"
        user = message.author
        if len(message.content.split(" ")) > 2:
            user_id = message.content.split(" ")[-1]
            user_id = user_id[3:-1]
            user = await client.fetch_user(int(user_id))
        embedVar = discord.Embed(title="Peepee size machine", description="{}'s penis\n{}".format(user.name, penis_size), color=0x00ff00)
        await message.channel.send(embed=embedVar)
        if (i == 0):
            await message.channel.send('Apa kau ga malu, punya penis 8D?')

    elif message.content.lower() == 'sudah kontribusi':
        await message.channel.send('https://github.com/nugroho-s/jahyadi')

client.run(environ.get('BOT_TOKEN'))