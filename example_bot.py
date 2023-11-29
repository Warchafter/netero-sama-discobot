import discord
import os
# import logging
from dotenv import load_dotenv

load_dotenv()

# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guild_scheduled_events = True

client = discord.Client(intents=intents)

# client.run(token, log_handler=handler)
discord.utils.setup_logging()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('El bot'):
        await message.channel.send('Si soy!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$Events'):
#         await fetch_scheduled_events(*, with_counts=True)

@client.event
async def on_scheduled_event_create(event):
    await event.channel.send('An event was just created!')


client.run(os.getenv('DISCORD_BOT_TOKEN'))