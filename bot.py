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
async def print_user(event):
    print(event.author)

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
    if event.content.__contains__("loss"):
        await event.message.respond("|   \|l \n||  |_")
    if event.content.__contains__("lost"):
        await event.message.respond("|   \|l \n||  |_")



@bot.listen(hikari.GuildMessageCreateEvent)
async def MessageMentionResponse(event):
    username = str(event.author).translate({ord(i): None for i in '#1234567890'})
    x = randint(1, 6)
    if event.content.__contains__("<@1002374211215577160>") and x==1:
        await event.message.respond(("Hello, ")+(username)+(". How may I help?"))
    if event.content.__contains__("<@1002374211215577160>") and x==2:
        await event.message.respond(("How are you doing, ")+(username)+("?"))
    if event.content.__contains__("<@1002374211215577160>") and x==3:
        await event.message.respond(("What's up, ")+(username)+("?"))
    if event.content.__contains__("<@1002374211215577160>") and x==4:
        await event.message.respond(("Do you need me to do anything?"))
    if event.content.__contains__("<@1002374211215577160>") and x==5:
        await event.message.respond(("Hello, bestie."))
    if event.content.__contains__("<@1002374211215577160>") and x==6:
        await event.message.respond(("I have been summoned by ")+(username)+("."))


bot.run()

