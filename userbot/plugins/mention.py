from telethon.tl.types import ChannelParticipantsAdmins as cp

from userbot import catub

from ..helpers.utils import get_user_from_event, reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="(all)(?: |$)(.*)",
    command=("tagall", plugin_category),
    info={
        "header": "tags recent 100 persons in the group may not work for all",
        "usage": [
            "{tr}all <text>",
            "{tr}tagall",
        ],
    },
)
async def _(event):
    "To tag all."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(2)
    mentions = input_str or "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@catub.cat_cmd(
    pattern="report$",
    command=("report", plugin_category),
    info={
        "header": "To tags admins in group.",
        "usage": "{tr}report",
    },
)
async def _(event):
    "To tags admins in group."
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(chat, filter=cp):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@catub.cat_cmd(
    pattern="tagall ?(.*)",
    command=("tagall", plugin_category),
    info={
        "header": "Tag everyone in a group.",
        "description": "Mention everyone in the group (with/without custom text)",
        "options": "If you want text along with tags, use .tagall text",
        "usage": [
            "{tr}tagall",
            "{tr}tagall <text>",
        ],
        "examples": [
            "{tr}tagall",
            "{tr}tagall Hello!",
        ],
    },
)
async def _(tag):
    "To tag everyone in a group."

    if tag.pattern_match.group(1):
        tagall = tag.pattern_match.group(1)
    else:
        tagall = " "
    prsn1 = await reply_id(tag)
    chat = await tag.get_input_chat()
    a_ = 0
    await tag.delete()
    async for i in bot.iter_participants(chat):
        if a_ == 500:
            break
        a_ += 5
        await tag.client.send_message(
            tag.chat_id,
            "[{}](tg://user?id={}) {}".format(i.first_name, i.id, tagall),
            reply_to=prsn1,
        )
        sleep(0.1)


@catub.cat_cmd(
    pattern="tagadmin ?(.*)",
    command=("tagadmin", plugin_category),
    info={
        "header": "Tag all admins in a group.",
        "description": "Mention all the admins in the group (with/without custom text)",
        "options": "If you want text along with tags, use .tagadmin text",
        "usage": [
            "{tr}tagadmin",
            "{tr}tagadmin <text>",
        ],
        "examples": [
            "{tr}tagadmin",
            "{tr}tagadmin Spam",
        ],
    },
)
async def _(tagadmin):
    "To tag every admin in a group"

    if tagadmin.pattern_match.group(1):
        tagtxt = tagadmin.pattern_match.group(1)
    else:
        tagtxt = " "
    prsn = await reply_id(tagadmin)
    chat = await tagadmin.get_input_chat()
    a_ = 0
    await tagadmin.delete()
    async for i in bot.iter_participants(chat, filter=cp):
        if a_ == 500:
            break
        a_ += 5
        await tagadmin.client.send_message(
            tagadmin.chat_id,
            "[{}](tg://user?id={}) {}".format(i.first_name, i.id, tagtxt),
            reply_to=prsn,
        )
        sleep(0.5)


@catub.cat_cmd(
    pattern="men (.*)",
    command=("mention", plugin_category),
    info={
        "header": "Tags that person with the given custom text.",
        "usage": [
            "{tr}men username/userid text",
            "text (username/mention)[custom text] text",
        ],
        "examples": ["{tr}men @mrconfused hi", "Hi @mrconfused[How are you?]"],
    },
)
async def _(event):
    "Tags that person with the given custom text."
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={user.id}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )
