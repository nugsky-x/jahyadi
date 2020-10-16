import discord
import json
from pprint import pprint
import logging
import random
from os import environ
import re

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
prefix = "sudah"

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

    if '750726551762370680>' in message.content:
        await message.channel.send('Kalau mau aku baikan, dont ever tag me!!')

    elif message.content.lower() == 'p':
        await message.channel.send('Apa kau ga malu, salam pakai P?')

    comparator_prefix = message.content[:len(prefix)].lower()
    if comparator_prefix != prefix:
        return

    args = message.content.lower().split(' ')

    if args[1] == "quote":
        await message.channel.send(random.choice(quotes))

    elif args[1] == "penis":
        await client.wait_until_ready()
        i = random.randint(0, 10)
        penis_size = "8" + ("=" * i) + "D"
        user = message.author
        if len(args) > 2:
            user_id = args[2]
            user_id = re.findall("\d+", user_id)[0]
            try:
                user = await client.fetch_user(int(user_id))
            except discord.errors.NotFound:
                logging.error("User not found: {}".format(user_id))
                return
        embed_var = discord.Embed(title="Peepee size machine",
                                  description="{}'s penis\n{}".format(user.name, penis_size), color=0x00ff00)
        await message.channel.send(embed=embed_var)
        if i == 0:
            await message.channel.send('Apa kau ga malu, punya penis 8D?')

    elif args[1] == 'kontribusi':
        await message.channel.send('https://github.com/nugroho-s/jahyadi')


client.run(environ.get('BOT_TOKEN'))
