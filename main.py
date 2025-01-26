#capture which user made which command, and the results that came from that command
#datetime_date, datetime_time, user, command_type, values_returned


import discordbot_secrets
import discord

bot_login = discordbot_secrets.DISCORDKEY

# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello {message.author}!')

client.run(bot_login)
