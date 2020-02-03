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


@bot.command(name='meme')
async def meme(ctx, template_id: int, caption0: str, caption1: str):
  url = 'https://api.imgflip.com/caption_image'
  params = dict(template_id=template_id, username=acc_username, password=acc_password, text0=caption0, text1=caption1)
  res = requests.get(url, params=params)

  data = res.json()

  print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
        "\nMeme: " + str(data['data']['url']))
    
  await ctx.send(data['data']['url'])

@bot.command(name='meme_templates')
async def meme(ctx):
  await ctx.send('https://api.imgflip.com/popular_meme_ids')

bot.run(token)
