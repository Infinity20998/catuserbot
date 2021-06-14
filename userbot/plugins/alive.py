# plugin edited by @Infinity20998
import random
import re
import time
from platform import python_version

import requests
from telethon import version
from telethon.events import CallbackQuery

from userbot import StartTime, catub, catversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"


@catub.cat_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status.",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm\n Random anime quotes will be shown if CUSTOM_ALIVE_TEXT is not set.",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    data = requests.get("https://animechan.vercel.app/api/random").json()
    anime = data["anime"]
    character = data["character"]
    quote = data["quote"]
    "To check your bot alive status."
    reply_to_id = await reply_id(event)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    ANIME = f"**“{quote}” - {character} ({anime})**"
    EMOJI = gvarstatus("ALIVE_EMOJI") or "〣"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ANIME
    CAT_IMG = gvarstatus("ALIVE_PIC")
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"**{ALIVE_TEXT}**\n\n"
        cat_caption += f"**{EMOJI} Sama:** {mention}\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"**{ALIVE_TEXT}**\n\n" f"**{EMOJI} Sama:** {mention}\n",
        )


@catub.cat_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "〣"
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, cat_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@catub.cat_cmd(
    pattern="calive$",
    command=("calive", plugin_category),
    info={
        "header": "To check bot's statistics",
        "usage": [
            "{tr}calive",
        ],
    },
)
async def amireallyalive(event):
    "To check bot's statistics."
    await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "〣"
    await edit_or_reply(
        event,
        f"**𝙏𝙝𝙚 𝙨𝙩𝙖𝙩𝙨 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙘𝙖𝙩𝙪𝙨𝙚𝙧𝙗𝙤𝙩 𝙖𝙧𝙚 :**\n\n"
        f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
        f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
        f"**{EMOJI} Python Version :** `{python_version()}\n`"
        f"**{EMOJI} Uptime :** `{uptime}\n`",
    )


@catub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
