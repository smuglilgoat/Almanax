import discord
from discord.ext import commands
import os

import datetime
import json

from keep_alive import keep_alive

client = commands.Bot(command_prefix = '$')
with open('almanax.json') as f:
  almanax = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def day(ctx):
  now = datetime.datetime.now()
  today = '{}-{:02d}-{:02d}'.format(now.year, now.month, now.day)
  today_almanax = almanax['{:02d}/{:02d}'.format(now.day, now.month)]
  image_id = today_almanax['itemImage']
  embed=discord.Embed(
    title=today_almanax["type"], 
    url=f'http://www.krosmoz.com/fr/almanax/{today}', 
    description=today_almanax["effect"],
    color=0xe4bf07)
  embed.set_author(name=today_almanax["quest"])
  embed.set_thumbnail(url=f'http://static.ankama.com/dofus/www/game/items/200/{image_id}.png')
  embed.add_field(
    name=today_almanax['offering'], 
    value=now, 
    inline=False)
  await ctx.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))