import discord
import os
import datetime
import json

client = discord.Client()
with open('almanax.json') as f:
  almanax = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$day'):
        now = datetime.datetime.now()
        today_almanax = almanax['{:02d}/{:02d}'.format(now.day, now.month)]
        await message.channel.send(today_almanax)
    
    if message.content.startswith('$week'):
        await message.channel.send('ble39el calmi rohek wach :peepoWTF:!')
    
    if message.content.startswith('$month'):
        await message.channel.send('ble39el calmi rohek wach :peepoWTF:!')

client.run(os.getenv('TOKEN'))
