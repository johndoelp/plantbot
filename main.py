#capture which user made which command, and the results that came from that command
#datetime_date, datetime_time, user, command_type, values_returned

#import libraries
import discordbot_secrets
import discord
from discord.ext import commands
import random
import moisture_scr
import picsnap_scr

#define botkey, listening channel
bot_login = discordbot_secrets.DISCORDKEY
bot_channel = 1332750253958500414

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

@bot.command(description='Says hello back to the user.')
async def hello(ctx):
    if ctx.author == bot.user:
        return

    else:
        if ctx.channel.id == bot_channel:
            print(f'Hello called by {ctx.author}.')
            await ctx.channel.send(f'Hello {ctx.author}!')

@bot.command(description='Rolls for a number between 0 - 100.')
async def roll(ctx):
    if ctx.channel.id == bot_channel:
        print(f'Roll called by {ctx.author}.')
        await ctx.channel.send(f'Rolled for {random.randint(0,100)}.')

@bot.command(description='Captures current moisture data for the plant.')
async def moisture(ctx):
    if ctx.channel.id == bot_channel:
        print(f'Moisture called by {ctx.author}.')
        await ctx.channel.send(f'Plant\'s current moisture is {moisture_scr.grab_moisture()}.')

@bot.command(description='Takes a picture and sends it to chat.')
async def pic(ctx):
    if ctx.channel.id == bot_channel:
        captured_img = picsnap_scr.pic_capture()
        plantpic = discord.File(captured_img, filename = "plantpic.jpg")
        print(f'Pic called by {ctx.author}.')
        await ctx.channel.send(file=plantpic)

bot.run(bot_login)
