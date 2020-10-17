import json
import logging
import random
from os import environ

import discord

from Kontribusi import Kontribusi
from Penis import Penis

logging.basicConfig(format='[%(levelname)s] [%(name)s] %(message)s', level=logging.INFO)
prefix = "sudah"

client = discord.Client()

commandhandlers = {
                    "penis": Penis(client, logging),
                    "kontribusi": Kontribusi()
                  }

with open('quotes.json') as json_file:
    quotes = json.load(json_file)


@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))


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

    if args[1] in commandhandlers:
        await commandhandlers[args[1]].do_response(message, args)

    # if args[1] == "quote":
    #     await message.channel.send(random.choice(quotes))
    #
    # elif args[1] == "penis":
    #     await Penis(client,logging).doresponse(message, args)
    #
    # elif args[1] == 'kontribusi':
    #     await message.channel.send('https://github.com/nugroho-s/jahyadi')


client.run(environ.get('BOT_TOKEN'))
