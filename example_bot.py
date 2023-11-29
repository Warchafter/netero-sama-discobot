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
intents.members = True

bot = discord.Client(intents=intents)

# client.run(token, log_handler=handler)
discord.utils.setup_logging()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('El bot'):
        await message.channel.send('Si soy!')

@bot.event
async def print_message(event):
    print(event.content)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$Events'):
#         await fetch_scheduled_events(*, with_counts=True)

@bot.event
async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.event
async def on_scheduled_event_create(self, event):
    await event.system_channel.send(f'An event was just created by ${event.creator}!')


bot.run(os.getenv('DISCORD_BOT_TOKEN'))