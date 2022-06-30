import discord
import requests
import json
import time
from keep_alive import keep_alive

TOKEN = 'YOUR TOKEN'

client = discord.Client()

# INPUT WORDS AND ADD WHATEVER U WANT😊
greeting_words = ["hai", "hello", "hi", "halo"]

time_words = ["time", "jam", "date", "hari", "waktu", "bulan", "tanggal"]

good_morning = ["pagi", "morning"]

good_evening = ["siang", "evening"]

good_night = ["night", "malam"]

bad_words = [""] #BAD WORDS

bye_words = ["bye", "dadah", "see you", "sampai jumpa"]


#get a current time
def get_localtime():
  global time
  localtime = str(time.asctime(time.localtime(time.time())))
  time = localtime
  return time

#get a random quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have loggend in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #EXAMPLE📄
  #if any(word in msg for word in YOUR WORDS):
  #  await message.channel.send(YOUR MESSAGE)
  
  if any(word in msg for word in greeting_words):
    await message.channel.send('Hi Everyone~!@\nWelcome to Programming Server :)')

  if msg.startswith('jichu'):
    await message.channel.send('Ada apa sih panggil  aku mulu~~! o(≧v≦)o')

  if any(word in msg for word in time_words):
    time = get_localtime()
    await message.channel.send(f'Local current time: {time}')

  if msg.startswith('$quote'):
    quote = get_quote()
    await message.channel.send((quote))

  if any(word in msg for word in good_morning):
    await message.channel.send(f'Good Morning Everyone~!@\n{client.user} Udah Bangun :)')

  if any(word in msg for word in good_evening):
    await message.channel.send(f'Good Evening Everyone~!@\n{client.user} Mau Main Dulu :)')

  if any(word in msg for word in good_night):
    await message.channel.send(f'Good Night Everyone~!@\n{client.user} Mau Tidur :)')

  if msg.startswith('bot'):
    await message.channel.send('Yaps Captain~!@,How can i help you? :)')

  if any(word in msg for word in bad_words):
    await message.channel.send('Caps~!@\nNo Bad Words Allowed!!! :|')

  if any(word in msg for word in bye_words):
    await message.channel.send('Good Bye~@ \nSampai Ketemu lagi~! o(≧v≦)o ')

  if any(word in msg for word in hs_words):
    await message.channel.send('Ada apa sayang? (⁎⁍̴̛ᴗ⁍̴̛⁎) ~!@')

  if any(word in msg for word in c_words):
    await message.channel.send('Makasih (⁎⁍̴̛ᴗ⁍̴̛⁎) ~!@')

keep_alive()
client.run(TOKEN)
