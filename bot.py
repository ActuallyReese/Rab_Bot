import hikari
from random import *
import requests
import json
import pandas as pd
from datetime import date

from config import Hikari_Key, Api_Key, WORDNIK_API_KEY


bot = hikari.GatewayBot(token=
Hikari_Key
)

current_date = date.today()


#code for using Wordnik api from https://www.twilio.com/blog/word-of-the-day-sms-python-twilio
def get_word_of_the_day(current_date):
    """
    Fetch word of the day from the Wordnik API
    """
    response_data = {"Word": "Sorry, No new word today", "Definition": "No definition available"}
    if WORDNIK_API_KEY:
        url = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?date={current_date}" \
              f"&api_key={WORDNIK_API_KEY}"
        response = requests.get(url)
        api_response = json.loads(response.text)
        if response.status_code == 200:
            response_data["Word"] = api_response["Word"]
            for definition in api_response["definitions"]:
                response_data["Definition"] = definition["text"]
                break
    else:
        # use a mock word if there is no Wordnik API key
        response_data["Word"] = "Mesmerizing"
        response_data["Definition"] = "Capturing one's attention as if by magic"
    return response_data
    


#prints the message author's username
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_user(event):
    print(event.author)

#prints the message
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

#prints to console once the bot has started
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

#Randomly responds and reacts to messages
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

#Responds to a specific set of words
@bot.listen(hikari.GuildMessageCreateEvent)
async def Loss(event):
    if event.content.__contains__("loss"):
        await event.message.respond("|   \|l \n||  |_")
    if event.content.__contains__("lost"):
        await event.message.respond("|   \|l \n||  |_")
    if event.content.__contains__("Lost"):
        await event.message.respond("|   \|l \n||  |_")
    if event.content.__contains__("Loss"):
        await event.message.respond("|   \|l \n||  |_")

#Responds when mentioned (@RabBot) and will message the word of the day if a message contains both "@RabBot" and "wotd"
@bot.listen(hikari.GuildMessageCreateEvent)
async def MessageMentionResponse(event):
    username = str(event.author).translate({ord(i): None for i in '#1234567890'})
    words = (get_word_of_the_day(current_date))
    x = randint(1, 7)
    if event.content.__contains__("<@1002374211215577160>"):
        if event.content.__contains__("wotd"):
            await event.message.respond("**Today's Word: **"+words['Word']+"\n**Definition: **"+words['Definition'])
        else:
        
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
            if event.content.__contains__("<@1002374211215577160>") and x==7:
                await event.message.respond(("L + ratio + fell off"))


bot.run()

