from discord.errors import Forbidden


async def try_send(channel, content=None, embed=None):
    try:
        if content:
            await channel.send(content)
        elif embed:
            await channel.send(embed=embed)
    except Forbidden:
        pass
