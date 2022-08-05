import hikari
from random import *
import requests
import json
import pandas as pd

from config import Hikari_Key, Api_Key



bot = hikari.GatewayBot(token=
Hikari_Key
)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.listen(hikari.GuildMessageCreateEvent)
async def Bwaah(event):
    x = randint(1, 100)
    print("x is ", x)
    y = randint(1, 80)
    print("y is ", y)
    if event.content.startswith("") and x==2:
        await event.message.respond("Bwaaahh!")
    if event.content.startswith("") and y==2:
        await event.message.add_reaction("🅱️")
        await event.message.add_reaction("🇼")
        await event.message.add_reaction("🇦")
        await event.message.add_reaction("🅰️")
        await event.message.add_reaction("🇭")
        await event.message.add_reaction("❗")

@bot.listen(hikari.GuildMessageCreateEvent)
async def Loss(event):
    if event.content.startswith("loss"):
        await event.message.respond("|   \|l \n||  |_")
    if event.content.startswith("lost"):
        await event.message.respond("|   \|l \n||  |_")
 

bot.run()

