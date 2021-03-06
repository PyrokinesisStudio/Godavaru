import config
import aiohttp


def remove_html(string):
    return string.replace('&amp;', '&').replace("&lt;", '<').replace("&gt;", '>').replace('&quot;', '"').replace(
        '&#039;', "'")


def get_status_emoji(status, number):
    status_dict = {
        "online": [
            "💚",
            "<:online:398856032392183819>"
        ],
        "idle": [
            "💛",
            "<:idle:398856031360253962>"
        ],
        "dnd": [
            "❤",
            "<:dnd:398856030068670477>"
        ]
    }
    return status_dict[status][number]


def get_prefix(bot, msg):
    prefixes = []
    prefixes.append(msg.guild.me.mention)
    for p in config.prefix:
        prefixes.append(p)
    try:
        pref = bot.prefixes[str(msg.guild.id)]
        if not pref is None and not len(pref) == 0 and not pref == "":
            prefixes.append(pref)
    except KeyError:
        pass
    return prefixes


async def get(url, headers=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            return await resp.read()


async def post(url, headers=None, data=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, data=data) as resp:
            return await resp.read()