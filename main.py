import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad","SAD","Sad","sAD", "SAd" "depressed","Depressed","DEPRESSED", "Unhappy", "UNHAPPY", "unhappy", "angry", "ANGRY", "Angry", "Miserable", "MISERABLE", "miserable", "depressing"]
bad_words = ["fuck", "cunt"]
happy_words = ["pog", "amazing", "ily", "happy", "wholesome", "best"]
reaction = ['<:ducklove:955328384546791455>','<:Milk_Mocha:955335754131841035>', '<:milk_mocha_hug:955336262926082089>', '<:mochaBear:955336309310890005>', '<:MilkMochaUltraLove:955336409621872670>', '<:mocha_milkdinolove:955336957666402374>', '<:chickjump:955337328413528125>' ]


starter_encouragements = [
  "Cheer up!",
  "You're really something special.",
  "Don’t care + didn’t ask + cry about it + stay mad + get real + L + mald seethe cope harder + ho mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + repelled + get a life + ok + and? + cringe + touch grass + donowalled + not based + your a (insert stereotype) + not funny didn’t laugh + you “re” + grammar issues + go outside + get good + reported + ad hominem + GG! + ask deez + ez clap + straight cash + ratio agian + final ratio + problematic",
  "Hang in there.",
  "You are an amazing person!"
]

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


  def get_insult():
    response = requests.get("https://insult.mattbas.org/api/insult.json")
    json_data = json.loads(response.text)
    insult = json_data['insult']
    return(insult)

  def get_compliment():
    response = requests.get("https://complimentr.com/api")
    json_data = json.loads(response.text)
    compliment = json_data['compliment']
    return(compliment)

  def doggie():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    doggie = json_data['message']
    return (doggie)

  def get_meme():
    response = requests.get("https://api.humorapi.com/memes/random")
    json_data = json.loads(response.text)
    meme = json_data['url'] 
    return (meme)

    
  def cat():
    response = requests.get("https://cataas.com/cat")
    json_data = json.loads(response.text)
    cat = json_data['url']
    return (cat)

  def joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    json_data = json.loads(response.text)
    joke = json_data['setup']+"\n" +"\n" +json_data['delivery']
    return (joke)
    
  def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      encouragements.append(encouraging_message)
      db["encouragements"] = encouragements
    else:
      db["encouragements"] = [encouraging_message]

  def get_shibe():
    response = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
    json_data = json.loads(response.text)
    shibe = json_data[0]
    return(shibe)
       

  msg = message.content
    


  if msg.startswith("!new"):
    encouraging_message = msg.split("!new ",1)[1]
    update_encouragements(encouraging_message)
    await message.reply("New encouraging message added.")

  if msg.startswith("!inspire"):
    await message.reply(get_quote())

  if msg.startswith("!del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("!del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.reply(encouragements.value)

  if msg.startswith("!list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.reply(encouragements.value)

  if msg.startswith("!responding"):
    value = msg.split("! responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.reply("Responding is on.")
    else:
      db["responding"] = False
      await message.reply("Responding is off.")

  if msg.startswith("!status"):
    await message.reply("We're at 200 lines of code now pog!!")
  
  if msg.startswith("!who are you"):
    await message.reply("I am a simple bot with very less functions which searches for sad words and returns an encouraging message. Also i give cool inspirational thingies. :D")
    
  if msg.startswith("!hello"):
    await message.reply("Hello!!", mention_author=True)

  if msg.startswith("!insult"):
    await message.reply(get_insult())
  
  if msg.startswith("!shibe"):
    await message.reply(get_shibe())

  if any(word in message.content for word in bad_words):
    await message.delete(delay=2)
    
  if any(word in message.content for word in happy_words):
    await message.add_reaction(random.choice(reaction))

  if msg.startswith("!nuke"):
    await message.channel.delete()

  if any(word in message.content for word in sad_words):
    await message.add_reaction('<:ducklove:955328384546791455>')
    await message.author.send(get_compliment()) 

  if msg.startswith("!doggo"):
    await message.reply(doggie())

  if msg.startswith("!insult"):
    await message.reply(get_insult())

  if msg.startswith("!compliment"+discord.Member.mention):
    response = discord.Member.mention+(get_compliment())
    await message.channel.send(response)
    

  if msg.startswith("!cat"):
    await message.reply(cat())

  if msg.startswith("!joke"):
    await message.reply(joke())

  if msg.startswith("!meme"):
    await message.reply(get_meme())

  if msg.startswith("!echo"):
    value = msg.split("!echo ",1)[1]
    if value == "on":
      db["echo"] = True
      await message.reply("Echo-ing is on.")
    else:
      db["echo"] = False
      await message.reply("Echo-ing is off.")

  if db["echo"] == True:
    if msg.startswith (""):
      await message.reply(message.content)

  if msg.startswith("!echo on"):
      if db["echo"] == True:
        await message.reply("Echo is already on")  
      if db["echo"] == False:
        await message.reply("Echo is already off")

  if msg.startswith("gm"):
    await message.reply("How are you?")
    await message.channel.send("How was your sleep?")
    

    

        

    


keep_alive()

client.run(os.getenv('TOKEN'))