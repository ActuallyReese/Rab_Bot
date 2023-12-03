import hikari
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
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


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
@bot.listen(hikari.MessageCreateEvent)
async def WordRespond(event):
    if re.search("(?i)([^A-Z]?L[^A-Z]?o[^A-Z]?s[^A-Z]?s[^A-Z]?)|([^A-Z]?l[^A-Z]?o[^A-Z]?s[^A-Z]?t[^A-Z]?)|([^A-Z]?l[^A-Z]?o[^A-Z]?s[^A-Z]?e[^A-Z]?)",event.content):
        await event.message.respond("|   \|l \n||  |_")
    if re.search("(?i)([^A-Z]?a[^A-Z]?m[^A-Z]?e[^A-Z]?r[^A-Z]?i[^A-Z]?c[^A-Z]?a[^A-Z]?)|([^A-Z]?u[^A-Z]?s[^A-Z]?a[^A-Z]?)|([^A-Z]?f[^A-Z]?r[^A-Z]?e[^A-Z]?e[^A-Z]?)",event.content):
            await event.message.add_reaction("🇲🇾")


        
#Responds when mentioned (@RabBot)
@bot.listen(hikari.MessageCreateEvent)
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
@bot.listen(hikari.MessageCreateEvent)
async def WordOfTheDay(event):
    current_date = date.today()
    words = (get_word_of_the_day(current_date))
    wordsCap = words['word'].capitalize()
    if event.content.startswith("Rwotd") or event.content.startswith("rwotd"):
        await event.message.respond("**Today's Word: **"+wordsCap+" \n**Category: **"+words['partOfSpeech'].capitalize()+"\n**Definition: **"+words['definition']+"\n**Note: **"+words['note'], tts=Toggle)

#Flips a coin
@bot.listen(hikari.MessageCreateEvent)
async def Coinflip(event):

    if event.content.startswith("Rcoinflip") or event.content.startswith("rcoinflip"):
        coin = randint(1, 2) 
        print("coin is ", coin)
        if coin==1:
            await event.message.respond("The coin landed on Heads", tts=Toggle, reply=True)
        if coin==2:
            await event.message.respond("The coin landed on Tails", tts=Toggle, reply=True)


#Reacts to specific users
@bot.listen(hikari.MessageCreateEvent)
async def Coins(event):
    react = randint(1, 20)
    if event.author_id==514109465675694091 and react == 2 or event.author_id==175768537779011584 and react == 2:
        await event.message.add_reaction("👎")
    if event.author_id==528032224491208706 and react == 2 or event.author_id==109090434059341824 and react == 2:
        await event.message.add_reaction("🔥")


#Stable Diffusion
@bot.listen(hikari.MessageCreateEvent)
async def Picture(event):
    STABILITY_HOST = 'grpc.stability.ai:443'

    if event.content.startswith("Rdraw") or event.content.startswith("rdraw"):
        rprompt = (event.content + " add a rabbit").replace("rdraw", "")
        #await event.message.respond("I can't do that at the moment; I'm sorry")
        chance = randint(1, 2)
        if chance == 1:
            await event.message.respond("One moment, please :)")
        elif chance == 2:
            await event.message.respond("Coming right up!")
        print(rprompt)


#################################################################################

            # Set up our connection to the API.
        stability_api = client.StabilityInference(
        key= STABILITY_KEY, # API Key reference.
        verbose=True, # Print debug messages.
        engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
        # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
        # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
        )


        answers = stability_api.generate(
            prompt= rprompt,
            #seed=992446758, # If a seed is provided, the resulting generated image will be deterministic.
                            # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
                            # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
            steps=30, # Amount of inference steps performed on image generation. Defaults to 30.
            cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                        # Setting this value higher increases the strength in which it tries to match your prompt.
                        # Defaults to 7.0 if not specified.
            width=512, # Generation width, defaults to 512 if not included.
            height=512, # Generation height, defaults to 512 if not included.
            samples=1, # Number of images to generate, defaults to 1 if not included.
            sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                        # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                        # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m)
        )

        # Set up our warning to print to the console if the adult content classifier is tripped.
        # If adult content classifier is not tripped, save generated images.

        filter = "off"
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                    imagebot =""
                    await event.message.respond("Whoops I can't draw that! Sorry D:")
                    event.message.respond("W")
                    print("sad")
                    filter = "on"
                    break
                if artifact.type == generation.ARTIFACT_IMAGE:
                    filter = "off"
                    img = Image.open(io.BytesIO(artifact.binary))
                    img2 = img.save("imagebot.png") # Save our generated images with their seed number as the filename.
                    print("success")

                
            
        if filter == "off":
            imagebot = "imagebot.png"
            await event.message.respond(attachment= imagebot)
            filter = "on"




#################################################################




#Displays all of the commands
@bot.listen(hikari.MessageCreateEvent)
async def Commands(event):

    if event.content.startswith("Rcommands") or event.content.startswith("rcommands"):
        await event.message.respond("The commands are: 'Rcommands', 'Rcoinflip', 'Rdraw', and 'Rwotd'. For Rdraw, tell me something you would like for me to draw", reply=True)





#




def go():
    bot.run()


# #def startThread():
#     #rab.start()

def stop():
     bot.join()







# create and configure a new thread
#rab = threading.Thread(target=go, daemon=True)

# wait for the new thread to finish


root = Tk()
root.title("RabBot")

mainframe = ttk.Frame(root, padding="43 43 52 52")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Start RabBot", command=go).grid(column=1, row=1, sticky=W)

ttk.Button(mainframe, text="Stop RabBot", command=stop).grid(column=2, row=1, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    

root.mainloop()