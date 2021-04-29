"""
Created by @Jisan7509
plugin for Cat_Userbot
☝☝☝
You remove this, you gay.
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import mention

 
@bot.on(admin_cmd("iascii ?(.*)"))
@bot.on(sudo_cmd(pattern="iascii ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "```Reply to any user message.```",time=6)
        return
    reply_message = await event.get_reply_message()
    if not reply_message.photo:
        await edit_delete(event, "```Reply to a picture...```",time=6)
        return
    chat = "@asciiart_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    kakashi = await edit_or_reply(event, "```Wait making ASCII...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164766745)
            )
            msg = await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @asciiart_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await kakashi.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await kakashi.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**➥ Image Type :** ASCII Art\n**➥ Uploaded By :** {mention}",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
    await event.client.delete_messages(conv.chat_id, [msg.id, response.id])


@bot.on(admin_cmd(pattern="line ?(.*)"))
@bot.on(sudo_cmd(pattern="line ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "```Reply to any user message.```",time=6)
        return
    reply_message = await event.get_reply_message()
    if not reply_message.photo:
        await edit_delete(event, "```Reply to a picture...```",time=6)
        return
    chat = "@Lines50Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    kakashi = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            pic = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @Lines50Bot and try again```")
            return
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            pic,
            caption=f"**➥ Image Type :** LINE Art \n**➥ Uploaded By :** {mention}",
        )
    await event.client.delete_messages(conv.chat_id, [msg.id, pic.id])


@bot.on(admin_cmd(pattern="clip ?(.*)"))
@bot.on(sudo_cmd(pattern="clip ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "```Reply to any user message.```",time=6)
        return
    reply_message = await event.get_reply_message()
    if not reply_message.photo:
        await edit_delete(event, "```Reply to a picture...```",time=6)
        return
    chat = "@clippy"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    kakashi = await edit_or_reply(event, "```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg= await conv.send_message(reply_message)
            pic = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @clippy and try again```")
            return
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            pic,
        )
    await event.client.delete_messages(conv.chat_id, [msg.id, pic.id])
    
    
    
CMD_HELP.update(
    {
        "art_img": "__**PLUGIN NAME :** Art Image__\
      \n\n📌** CMD ➥** `.iascii` reply to any image file:\
      \n**USAGE   ➥  **Makes an image ascii style, try out your own.\
      \n\n📌** CMD ➥** `.line` reply to any image file:\
      \n**USAGE   ➥  **Makes an image line style.\
      \n\n📌** CMD ➥** `.clip` reply to any image file:\
      \n**USAGE   ➥  **Makes a stylish sticker."
    }
)
