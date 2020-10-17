import json
import random

from util.Util import try_send


class Quote:
    def __init__(self):
        with open('quotes.json') as json_file:
            self.quotes = json.load(json_file)

    async def do_response(self, message, args):
        await try_send(message.channel, random.choice(self.quotes))
