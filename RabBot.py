# This example requires the 'message_content' intent.

import discord
import asyncio
from random import *
import requests
import json
import pandas as pd
import re
from datetime import date, datetime
import time
import schedule
from tkinter import *
from tkinter import ttk
import threading
from threading import Event


from config import Hikari_Key, Api_Key, WORDNIK_API_KEY, STABILITY_KEY
from animalfact import get_panda


import os
import io
import warnings
#from PIL import Image
#from stability_sdk import client
#import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

current_date = date.today()

Toggle = "False"

#code for using Wordnik api from https://www.twilio.com/blog/word-of-the-day-sms-python-twilio
def get_word_of_the_day(current_date):
    """
    Fetch word of the day from the Wordnik API
    """
    current_date = date.today()
    response_data = {"word": "Sorry, No new word today", "partOfSpeech": "No part of speech", "definition": "No definition available", "note": "No notes"}
    if WORDNIK_API_KEY:
        url = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?date={current_date}" \
              f"&api_key={WORDNIK_API_KEY}"
        response = requests.get(url)
        api_response = json.loads(response.text)
        if response.status_code == 200:
            response_data["word"] = api_response["word"]
            response_data["note"] = api_response["note"]
            for definition in api_response["definitions"]:
                response_data["definition"] = definition["text"]
                response_data["partOfSpeech"] = definition["partOfSpeech"]
                break
    else:
        # use a mock word if there is no Wordnik API key
        response_data["word"] = "mesmerizing"
        response_data["partOfSpeech"] = "adjective"
        response_data["definition"] = "capturing one's attention as if by magic"
        response_data["note"] = "n/a"
    return response_data
    print(current_date)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("hi")

    if message.content.startswith(""):
        print(message.author, ":", message.content)
        x = randint(1, 500)
        print("x is ", x)
        y = randint(1, 200)
        print("y is ", y)

#Randomly responds and reacts to messages
    if message.content.startswith("") and x==2:
        await message.channel.send("Bwaaahh!")
        
    if message.content.startswith("a") and y==2:
        await message.add_reaction("🅱️")
        await message.add_reaction("🇼")
        await message.add_reaction("🇦")
        await message.add_reaction("🅰️")
        await message.add_reaction("🇭")
        await message.add_reaction("❗")
    
    # await client.process_commands(message)


# @client.event
# async def on_message(message):
    # if message.content.__contains__("h"):
    #     await message.add_reaction("❗")

        
    # await client.process_commands(message)

#Will respond with the word of the day if the message is "rwotd"
    current_date = date.today()
    words = (get_word_of_the_day(current_date))
    wordsCap = words['word'].capitalize()
    if message.content.startswith("Rwotd") or message.content.startswith("rwotd"):
        await message.channel.send("**Today's Word: **"+wordsCap+" \n**Category: **"+words['partOfSpeech'].capitalize()+"\n**Definition: **"+words['definition']+"\n**Note: **"+words['note'])


# @client.event
# async def on_message(message):
    if message.content.startswith("Rcoinflip") or message.content.startswith("rcoinflip"):
        coin = randint(1, 2) 
        print("coin is ", coin)
        if coin==1:
            await message.channel.send("The coin landed on Heads")
        if coin==2:
            await message.channel.send("The coin landed on Tails")



    # STABILITY_HOST = 'grpc.stability.ai:443'

    # if message.content.startswith("Rdraw") or message.content.startswith("rdraw"):
    #     rprompt = (message.content + " add a rabbit").replace("rdraw", "")
    #     #await event.message.respond("I can't do that at the moment; I'm sorry")
    #     chance = randint(1, 2)
    #     if chance == 1:
    #         await message.reply("One moment, please :)")
    #     elif chance == 2:
    #         await message.reply("Coming right up!")
    #     print(rprompt)


#################################################################################

            # Set up our connection to the API.
        # response = requests.post(
        # f"https://api.stability.ai/v2beta/stable-image/generate/core",
        # headers={
        #     "authorization": STABILITY_KEY,
        #     "accept": "image/*"
        # },
        # files={"none": ''},
        # data={
        #     "prompt": rprompt,
        #     "output_format": "png",
        # },
        # )

        # if response.status_code == 200:
        #     with open("./images/" + rprompt + ".png", 'wb') as file:
        #         file.write(response.content)
        #     await message.send(file = response.content)
        # else:
        #     await message.reply("Oops all out of tokens")
        #     raise Exception(str(response.json()))
            

#################################################################

    # print all commands

    if message.content.startswith("Rcommands") or message.content.startswith("rcommands"):
        await message.reply("The commands are: 'Rcommands', 'Rcoinflip', 'Rdraw', and 'Rwotd'. For Rdraw, tell me something you would like for me to draw")
    

    # Loss and freedom haha

    if re.search("(?i)([^A-Z]?L[^A-Z]?o[^A-Z]?s[^A-Z]?s[^A-Z]?)|([^A-Z]?l[^A-Z]?o[^A-Z]?s[^A-Z]?t[^A-Z]?)|([^A-Z]?l[^A-Z]?o[^A-Z]?s[^A-Z]?e[^A-Z]?)",message.content):
        await message.reply("|   \|l \n||  |_")
    if re.search("(?i)([^A-Z]?a[^A-Z]?m[^A-Z]?e[^A-Z]?r[^A-Z]?i[^A-Z]?c[^A-Z]?a[^A-Z]?)|([^A-Z]?u[^A-Z]?s[^A-Z]?a[^A-Z]?)|([^A-Z]?f[^A-Z]?r[^A-Z]?e[^A-Z]?e[^A-Z]?)",message.content):
            await message.add_reaction("🇲🇾")

    
    # responds to people @ing it
    
    username = str(message.author).translate({ord(i): None for i in '#1234567890'})
    x = randint(1, 7)
    if message.content.__contains__("<@1002374211215577160>") or message.content.__contains__("rabbot") or message.content.__contains__("Rabbot") or message.content.__contains__("RabBot"):
        if message.content.__contains__("thank you") or message.content.__contains__("thanks") or message.content.__contains__("Thank you") or message.content.__contains__("Thanks"): 
            await message.reply("You're welcome :)")    
        elif message.content.__contains__("<@1002374211215577160>") and x==1:
            await message.reply(("Hello, ")+(username)+(". How may I help?"))
        elif message.content.__contains__("<@1002374211215577160>") and x==2:
            await message.reply(("How are you doing, ")+(username)+("?"))
        elif message.content.__contains__("<@1002374211215577160>") and x==3:
            await message.reply(("What's up, ")+(username)+("?"))
        elif message.content.__contains__("<@1002374211215577160>") and x==4:
            await message.reply(("Do you need me to do anything?"))
        elif message.content.__contains__("<@1002374211215577160>") and x==5:
            await message.reply(("Hello, bestie."))
        elif message.content.__contains__("<@1002374211215577160>") and x==6:
            await message.reply(("I have been summoned by ")+(username)+("."))
        elif message.content.__contains__("<@1002374211215577160>") and x==7:
            await message.reply(("L + ratio + fell off"))

@client.event
async def message_print(message):
    print(message.author)

client.run(Hikari_Key)