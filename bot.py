import hikari
from random import *
import requests
import json
import pandas as pd
import re
from datetime import date

from config import Hikari_Key, Api_Key, WORDNIK_API_KEY
from animalfact import get_panda



bot = hikari.GatewayBot(token=
Hikari_Key
)

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
    

#Responds with random animal picture and fact (currently not working)
#@bot.listen(hikari.GuildMessageCreateEvent)
async def Panda(event):
    animals = [animalfact.get_panda(), animalfact.get_dog(), animalfact.get_birb(), animalfact.get_cat(), animalfact.get_fox(), animalfact.get_kangaroo(), animalfact.get_koala(), animalfact.get_raccoon(), animalfact.get_red_panda()]
    if event.content.__contains__("ranimal") or event.content.__contains__("ranimal"):
        i = randint(0, 8)
        animal = animals[i]
        await event.message.respond(animal['fact'], tts=Toggle)
        await event.message.respond(animal['image'])
        print(animal)


#prints the message author's username
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_user(event):
    print(event.author, event.author_id)

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
    x = randint(1, 500)
    print("x is ", x)
    y = randint(1, 200)
    print("y is ", y)
    if event.content.startswith("") and x==2:
        await event.message.respond("Bwaaahh!", tts=Toggle, reply=True)
    if event.content.startswith("") and y==2:
        await event.message.add_reaction("🅱️")
        await event.message.add_reaction("🇼")
        await event.message.add_reaction("🇦")
        await event.message.add_reaction("🅰️")
        await event.message.add_reaction("🇭")
        await event.message.add_reaction("❗")



#Responds to a specific set of words
@bot.listen(hikari.GuildMessageCreateEvent)
async def WordRespond(event):
    if re.search("(?i)(.?L.?o.?s.?s.?)|(.?l.?o.?s.?t.?)|(.?l.?o.?s.?e.?)",event.content):
        await event.message.respond("|   \|l \n||  |_")
    if re.search("(?i)(.?a.?m.?e.?r.?i.?c.?a.?)|(.?u.?s.?a.?)|(.?f.?r.?e.?e.?)",event.content):
            await event.message.add_reaction("🇲🇾")


        
#Responds when mentioned (@RabBot)
@bot.listen(hikari.GuildMessageCreateEvent)
async def MessageMentionResponse(event):
    username = str(event.author).translate({ord(i): None for i in '#1234567890'})
    x = randint(1, 7)
    if event.content.__contains__("<@1002374211215577160>") or event.content.__contains__("rabbot") or event.content.__contains__("Rabbot") or event.content.__contains__("RabBot"):
        if event.content.__contains__("thank you") or event.content.__contains__("thanks") or event.content.__contains__("Thank you") or event.content.__contains__("Thanks"): 
            await event.message.respond("You're welcome :)", tts=Toggle, reply=True)    
        elif event.content.__contains__("<@1002374211215577160>") and x==1:
            await event.message.respond(("Hello, ")+(username)+(". How may I help?"), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==2:
            await event.message.respond(("How are you doing, ")+(username)+("?"), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==3:
            await event.message.respond(("What's up, ")+(username)+("?"), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==4:
            await event.message.respond(("Do you need me to do anything?"), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==5:
            await event.message.respond(("Hello, bestie."), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==6:
            await event.message.respond(("I have been summoned by ")+(username)+("."), tts=Toggle, reply=True)
        elif event.content.__contains__("<@1002374211215577160>") and x==7:
            await event.message.respond(("L + ratio + fell off"), tts=Toggle, reply=True)


#Will respond with the word of the day if the message is "!wotd"
@bot.listen(hikari.GuildMessageCreateEvent)
async def WordOfTheDay(event):
    current_date = date.today()
    words = (get_word_of_the_day(current_date))
    wordsCap = words['word'].capitalize()
    if event.content.startswith("Rwotd") or event.content.startswith("rwotd"):
        await event.message.respond("**Today's Word: **"+wordsCap+" \n**Category: **"+words['partOfSpeech'].capitalize()+"\n**Definition: **"+words['definition']+"\n**Note: **"+words['note'], tts=Toggle)

#Flips a coin
@bot.listen(hikari.GuildMessageCreateEvent)
async def Coinflip(event):

    if event.content.startswith("Rcoinflip") or event.content.startswith("rcoinflip"):
        coin = randint(1, 2) 
        print("coin is ", coin)
        if coin==1:
            await event.message.respond("The coin landed on Heads", tts=Toggle, reply=True)
        if coin==2:
            await event.message.respond("The coin landed on Tails", tts=Toggle, reply=True)


#Reacts to specific users
@bot.listen(hikari.GuildMessageCreateEvent)
async def Coins(event):
    react = randint(1, 20)
    if event.author_id==514109465675694091 and react == 2 or event.author_id==175768537779011584 and react == 2:
        await event.message.add_reaction("👎")
    if event.author_id==528032224491208706 and react == 2 or event.author_id==109090434059341824 and react == 2:
        await event.message.add_reaction("🔥")


#Displays all of the commands
@bot.listen(hikari.GuildMessageCreateEvent)
async def Commands(event):

    if event.content.startswith("Rcommands") or event.content.startswith("rcommands"):
        await event.message.respond("The commands are: 'Rcommands', 'Rcoinflip', 'Ranimal', and 'Rwotd'", reply=True)

bot.run()

