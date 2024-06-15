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
from PIL import Image


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
    if message.content.__contains__("h"):
        await message.add_reaction("❗")

        
    # await client.process_commands(message)

# @client.event
# async def on_message(message):
    if message.content.startswith("Rcoinflip") or message.content.startswith("rcoinflip"):
        coin = randint(1, 2) 
        print("coin is ", coin)
        if coin==1:
            await message.channel.send("The coin landed on Heads")
        if coin==2:
            await message.channel.send("The coin landed on Tails")

    


@client.event
async def message_print(message):
    print(message.author)

client.run(Hikari_Key)