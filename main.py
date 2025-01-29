#capture which user made which command, and the results that came from that command
#datetime_date, datetime_time, user, command_type, values_returned

#import libraries
import discordbot_secrets
import discord
from discord.ext import commands
import random
import moisture

#define botkey
bot_login = discordbot_secrets.DISCORDKEY

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Plantbot is alive as {bot.user}!')
    print('------------------------------------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello {message.author}!')
    
    if message.content.startswith('!roll'):
        await message.channel.send(f'Rolled for {int(random(0,100))}.')
    
    if message.content.startswith('!moisture'):
        await message.channel.send(f'Plant\'s current moisture is {moisture.grab_moisture()}.')

bot.run(bot_login)
