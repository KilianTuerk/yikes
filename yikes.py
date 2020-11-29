# bot.py
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import logging
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
            await ctx.send("Das ist keine richtige Zeitangabe, du Ochogesicht :middle_finger:")
            return
        await ctx.send("Jo, aber ich pinge keinen!")
        time = time * 60
        while True:
            time = time - 1
            logging.info(time)
            if time == 0:
                await ctx.send(f"Die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")
                break
            await asyncio.sleep(1)

    else:
        time = int(time)
        if time <= 0:
            await ctx.send("Das ist keine richtige Zeitangabe, du Ochogesicht :middle_finger:")
            return
        pinged = ", ".join(x.mention for x in members)
        await ctx.send(f"Jo, ich werde {pinged} in {time} Minuten pingen und eine Nachricht schreiben (Auge dreamin' botto)!")
        time = time * 60
        while True:
            time = time - 1
            logging.info(time)
            if time == 0:
                await ctx.send(f"{pinged} Die Zeit ist abgelaufen! :disappointed_relieved: :point_right: :alarm_clock:\nNachricht: {message}")
                break
            await asyncio.sleep(1)

@bot.command()
async def dreaminbotto(ctx):
    await ctx.send("dreamin' botto stinkt :blush:")    

bot.run(TOKEN)


