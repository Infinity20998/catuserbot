#plugin edited by @Infinity20998
import time
import random
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "cat"
CAT_IMG = Config.ALIVE_PIC
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "

ANIME_QUOTE = [
"“If you don’t take risks, you can’t create a future!” – Monkey D. Luffy (One Piece)",
"“Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.” – Gildarts Clive (Fairy Tail)",
"“People’s lives don’t end when they die, it ends when they lose faith.” – Itachi Uchiha (Naruto)",
"“If you don’t like your destiny, don’t accept it.” – Naruto Uzumaki (Naruto)",
"“When you give up, that’s when the game ends.” – Mitsuyoshi Anzai (Slam Dunk)",
"“All we can do is live until the day we die. Control what we can…and fly free.” – Deneil Young (Uchuu Kyoudai or Space Brothers)","“Forgetting is like a wound. The wound may heal, but it has already left a scar.” – Monkey D. Luffy (One Piece)",
"“Giving up kills people. When people reject giving up… they finally win the right to transcend humanity.” – Alucard (Hellsing)",
"“If you don’t share someone’s pain, you can never understand them.” – Nagato (Naruto)",
"“Whatever you lose, you’ll find it again. But what you throw away you’ll never get back.“ – Himura Kenshin (Rurouni Kenshin)",
"“I’ll leave tomorrow’s problems to tomorrow’s me.” – Saitama (One-Punch Man)",
"“Being lonely is more painful then getting hurt.” – Monkey D. Luffy (One Piece)",
"“There’s no shame in falling down! True shame is to not stand up again!” – Shintarō Midorima (Kuroko’s Basketball)",
"“Why should I apologize for being a monster? Has anyone ever apologized for turning me into one?” – Juuzou Suzuya (Tokyo Ghoul)",
"“People become stronger because they have memories they can’t forget.” – Tsunade (Naruto)",
"“If you wanna make people dream, you’ve gotta start by believing in that dream yourself!” – Seiya Kanie (Amagi Brilliant Park)",
"“Simplicity is the easiest path to true beauty.” – Seishuu Handa (Barakamon)",
"“Don’t be so quick to throw away your life. No matter how disgraceful or embarrassing it may be, you need to keep struggling to find your way out until the very end.” – Clare (Claymore)","“The world’s not perfect, but it’s there for us trying the best it can. That’s what makes it so damn beautiful.” – Roy Mustang (Fullmetal Alchemist)",
"“If you can’t do something, then don’t. Focus on what you can.” – Shiroe (Log Horizon)",
"“It doesn’t do any good to pretend you can’t see what’s going on.” – Yuuya Mochizuki (Another)",
"“A dropout will beat a genius through hard work.” – Rock Lee (Naruto)",
"“Sometimes, people are just mean. Don’t fight mean with mean. Hold your head high.” – Hinata Miyake (A Place Further than the Universe)",
"“To act is not necessarily compassion. True compassion sometimes comes from inaction.” – Hinata Miyake (A Place Further than the Universe)",
"“When you hit the point of no return, that’s the moment it truly becomes a journey. If you can still turn back, it’s not really a journey.” – Hinata Miyake (A Place Further than the Universe)",
"“Being weak is nothing to be ashamed of… Staying weak is !!“ – Fuegoleon Vermillion (Black Clover)",
"“Reject common sense to make the impossible possible.”– Simon (Tengen Toppa Gurren Lagann)",
"“If you really want to be strong… Stop caring about what your surrounding thinks of you!”– Saitama (One Punch Man)",
"“Who decides limits? And based on what? You said you worked hard? Well, maybe you need to work a little harder. Is that really the limit of your strength? Could the you of tomorrow beat you today? Instead of giving in, move forward.”– Saitama (One Punch Man)",
"“A person grows up when he’s able to overcome hardships. Protection is important, but there are some things that a person must learn on his own.“– Jiraiya (Naruto)",
"“Hard work is worthless for those that don’t believe in themselves.”– Naruto Uzumaki (Naruto)",
"“Mistakes are not shackles that halt one from stepping forward. Rather, they are that which sustain and grow one’s heart.”– Mavis Vermillion (Fairy Tail)",
"“A place where someone still thinks about you is a place you can call home.”– Jiraiya (Naruto)",
"“Life comes at a cost. Wouldn’t it be arrogant to die before you’ve repaid that debt?”– Yuuji Kazami (The Fruit of Grisaia / Gurizaia no Kajitsu)",
"“Vision is not what your eyes see, but an image that your brain comprehends.”– Touko Aozaki (The Garden of Sinners / Kara no Kyōkai)",
"“Hatred and Sorrow are power. They are yours to control. All you have to do is to turn them into strength and use that strength to move forward.“– Sebastian Michaelis (Black Butler / Kuroshitsuji)",
"“It’s not always possible to do what we want to do, but it’s important to believe in something before you actually do it.”– Might Guy (Naruto)",
"“Don’t beg for things. Do it yourself, or else you won’t get anything.”– Renton Thurston (Eureka Seven)"
"“Life and death are like light and shadow. They’re both always there. But people don’t like thinking about death, so subconsciously, they always look away from it.”– Yato (Noragami)",
"“Moving on doesn’t mean you forget about things. It just means you have to accept what’s happened and continue living.“– Erza Scarlet (Fairy Tail)",
"“If you keep on hiding your true feelings, who is going to be happy? If you are sad, you should say it out loud!”– Haruhi Fujioka (Ouran High School Host Club)",
"“You can die anytime, but living takes true courage.”– Himura Kenshin (Rurouni Kenshin)","“Every journey begins with a single step. We just have to have patience.”– Milly Thompson (Trigun)",
"“If nobody cares to accept you and wants you in this world, accept yourself and you will see that you don’t need them and their selfish ideas.”– Alibaba Saluja (Universal Warriors)",
"“Don’t be upset because of what you can’t do. Do what you do best, live as carefree and optimistically as you can, because some people aren’t able to do that.”– Keima Katsuragi (The World God Only Knows)",
"“If you begin to regret, you’ll dull your future decisions and let others make your choices for you. All that’s left for you then is to die. Nobody can foretell the outcome. Each decision you make holds meaning only by affecting your next decision.”– Erwin Smith (Attack on Titan)",
"“Everything has a beginning and an end. Life is just a cycle of starts and stops. There are ends we don’t desire, but they’re inevitable, we have to face them. It’s what being human is all about.”– Jet Black (Cowboy Bebop)",
"“Anything can happen. No one ever thinks it will until it does. What will happen, happens. That’s how the world is. The most important thing is to not let the tragedy defeat you. To believe that you can get through it.”– Kyousuke Natsume (Little Busters!)",
"“You’ll only realize that you truly love someone if they already caused you enormous pain. Your enemies can never hurt you the way your loved ones can. It’s the people close to your heart that can give you the most piercing wound. Love is a double-edged sword, it can heal the wound faster or it can sink the blade even deeper.”– Himura Kenshin (Rurouni Kenshin)",
"“It is at the moment of death that humanity has value.”– Archer (Fate Series)",
"“A lesson without pain is meaningless. That’s because no one can gain without sacrificing something. But by enduring that pain and overcoming it, he shall obtain a powerful, unmatched heart.”– Edward Elric (Fullmetal Alchemist: Brotherhood)",
"“You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face.”– Roronoa Zoro (One Piece)",
]
    
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    ANIME = f"{random.choice(ANIME_QUOTE)}"
    CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or ANIME
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        cat_caption += f"**{EMOJI} Senpai :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()
    
   
@bot.on(admin_cmd(outgoing=True, pattern="salive$"))
@bot.on(sudo_cmd(pattern="salive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    await edit_or_reply(
            alive,
            f"**𝙏𝙝𝙚 𝙨𝙩𝙖𝙩𝙨 𝙤𝙛 𝙮𝙤𝙪𝙧 𝙘𝙖𝙩 𝙪𝙨𝙚𝙧𝙗𝙤𝙩 𝙖𝙧𝙚 :**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n",
        )

# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n  •  **Syntax : **`.alive` \
      \n  •  **Function : **__status of bot will be showed__\
      \n\n  •  **Syntax : **`.ialive` \
      \n  •  **Function : **__inline status of bot will be shown.__\
      \n\n  •  **Syntax : **`.salive` \
      \n  •  **Function : **__To check the stats of your bot.__\
      \n\nSet `ALIVE_PIC` var for media in alive message and set `IALIVE_PIC` for media in ialive message"
    }
)
