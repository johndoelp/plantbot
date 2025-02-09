#capture which user made which command, and the results that came from that command
#datetime_date, datetime_time, user, command_type, values_returned

#import libraries
import discordbot_secrets
import discord
from discord.ext import commands
import random
from grow.moisture import Moisture
from time import sleep

#camera setup
from picamera2 import Picamera2
from PIL import Image
import io
camera = Picamera2()
camera.configure(camera.create_still_configuration())
camera.start()

#define botkey, listening channel
bot_login = discordbot_secrets.DISCORDKEY
bot_channel = discordbot_secrets.CHANNELKEY

description = '''Plantbot: a Dicord bot run on a Raspberry Pi that detects
the moisture of a plant, waters the plant, takes a picture of the plant...

Run by commands in a Discord server.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

#capture moisture
def grab_moisture():
    #create list of moisture readings to avg
    moistures = []
    m1_sensor = Moisture(1)
    m1 = 0

    for i in range(10):
        while m1 == 0:
            m1 = m1_sensor.moisture
        moistures.append(m1)
        m1 = 0
        print(moistures)
        sleep(0.5)
    
    avg_moisture = round(sum(moistures) / len(moistures), 2)
    print(f'Average moisture is {avg_moisture}.')
    return(avg_moisture)

#capture picture
def grab_picture(camera):
    img_array = camera.capture_array()
    image = Image.fromarray(img_array)
    img_mem = io.BytesIO()
    image.save(img_mem, format = "JPEG")
    img_mem.seek(0)
    return img_mem


#discord bot commands
@bot.event
async def on_ready():
    print(f'Plantbot is alive as {bot.user}!')
    print('------------------------------------')

#hello test
@bot.command(description='Says hello back to the user.')
async def hello(ctx):
    if ctx.author == bot.user:
        return

    else:
        if ctx.channel.id == bot_channel:
            print(f'Hello called by {ctx.author}.')
            await ctx.channel.send(f'Hello {ctx.author}!')

#roll test
@bot.command(description='Rolls for a number between 0 - 100.')
async def roll(ctx):
    if ctx.channel.id == bot_channel:
        print(f'Roll called by {ctx.author}.')
        await ctx.channel.send(f'Rolled for {random.randint(0,100)}.')

#capture moisture
@bot.command(description='Captures current moisture data for the plant.')
async def moisture(ctx):
    if ctx.channel.id == bot_channel:
        print(f'Moisture called by {ctx.author}.')
        await ctx.channel.send(f'Plant\'s current moisture is {grab_moisture()}.')

#capture picture
@bot.command(description='Takes a picture and sends it to chat.')
async def pic(ctx):
    if ctx.channel.id == bot_channel:
        plantpic = discord.File(grab_picture(camera), filename = "plantpic.jpg")
        print(f'Pic called by {ctx.author}.')
        await ctx.channel.send(file=plantpic)

#captures moisture and picture, sends both in same message
@bot.command(description='Captures current moisture data for the plant.')
async def status(ctx):
    if ctx.channel.id == bot_channel:
        print(f'Status called by {ctx.author}.')
        plantpic = discord.File(grab_picture(camera), filename = "plantpic.jpg")
        temperature = "TBD"
        await ctx.channel.send(content=f'Plant\'s current moisture is {grab_moisture()}, and the temp is {temperature}.', file=plantpic)

bot.run(bot_login)
