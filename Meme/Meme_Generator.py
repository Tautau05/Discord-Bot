#!/usr/bin/env python3
import os
import requests
from datetime import datetime

import discord
from discord.ext import commands


#Discord Bot Token
token = ""
#imgflip account
acc_username = ""
acc_password = ""


client = discord.Client()

bot = commands.Bot(command_prefix='!')

async with aiohttp.ClientSession() as session:
    async with session.get('https://api.imgflip.com/get_memes') as r:
        if r.status == 200:
            memes = await r.json()['data']['memes']

@bot.command(name='meme')
async def meme(ctx, meme_id: str, *args):
  url = 'https://api.imgflip.com/caption_image'
  template_id = 0
  try:
      # Check if ID supplied
      template_id = int(meme_id)
  except ValueError:
      # If ID not supplied try to guess meme from name
      for meme in memes:
          if meme_id.casefold() in meme['name'].casefold():
              template_id = meme['id']
              break
  if template_id == 0:
    await ctx.send('Meme not found, check the ID with !meme_templates')
    return

  params = dict(template_id=template_id, username=acc_username, password=acc_password)
  for i, text in enumerate(args):
      params["text"+str(i)] = text
  async with aiohttp.ClientSession() as session:
      async with session.get(url, params=params) as r:
         data = r.json()

  print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
        "\nMeme: " + str(data['data']['url']))
    
  await ctx.send(data['data']['url'])

@bot.command(aliases=['templates'])
async def meme_templates(ctx):
  await ctx.send('https://api.imgflip.com/popular_meme_ids')

bot.run(token)
