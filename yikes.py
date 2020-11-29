# bot.py
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
#import logging
import asyncio
#import hilfe.py
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix='-')

@bot.command()
async def timer(ctx, time, members: commands.Greedy[discord.Member] = None, message = "Keine Nachricht angegeben"):   
    if not members:
        time = int(time)
        if time <= 0:
            await ctx.send("Das ist keine richtige Zeitangabe, du Ochogesicht :rage:")
            return
        await ctx.send("Jo, aber ich pinge keinen!")
        time = time * 60
        # while True:
        #     time = time - 1
        #     logging.info(time)
        #     if time == 0:
        #         await ctx.send(f"Die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")
        #         break
        #     await asyncio.sleep(1)
        await asyncio.sleep(time)
        await ctx.send(f"Die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")

    else:
        print(members)
        time = int(time)
        if time <= 0:
            await ctx.send("Das ist keine richtige Zeitangabe, du Ochogesicht :rage:")
            return
        member_pinged = " und ".join(x.mention for x in members)
        # displaymember = ""
        # for member in members:
        #     nickname = member.name if not member.nick else member.nick
        #     displaymember = " und ".join(nickname)
        #member = " und ".join(x.nick for x in members)
        await ctx.send(f"Jo, ich werde {member_pinged} in {time} Minuten pingen!")
        time = time * 60
        # while True:
        #     time = time - 1
        #     logging.info(time)
        #     if time == 0:
        #         await ctx.send(f"Ey, {member_pinged}, die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")
        #         break
        #     await asyncio.sleep(1)
        await asyncio.sleep(time)
        await ctx.send(f"Ey, {member_pinged}, die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")

@bot.command()
async def dreaminbotto(ctx):
    await ctx.send("dreamin' botto stinkt :blush:")    

bot.run(TOKEN)

#wenn man zwei user angibt und keine nachricht springt er in die zweite abfrage und sagt, dass er eine nachricht schreiben wird.


