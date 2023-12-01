import discord
import os
import datetime
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

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('test1'):
#             await ctx.send(f"The icon url is: {icon_url}")

async def get_server_icon_url(self, ctx):
    return ctx.guild.icon.url


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
async def on_scheduled_event_create(event):
    print("an event was created")
    channel = bot.get_channel(525353169178329119)
    # channel = bot.get_channel(1180161923120119840)
    embed = discord.Embed(
        colour=discord.Colour.blurple(),
        description= f"{event.description} \n -> {event.guild.default_role.mention}, join [here]({event.url})",
        title="New Event!"
    )
    timeFormat = event.start_time
    embed.add_field(name="Created By", value=event.creator.global_name, inline="true")
    embed.add_field(name="Location", value=event.channel.name, inline="true")
    embed.add_field(name="Time", value=timeFormat.strftime("%A %d. %H:%M"), inline="true")
    embed.set_thumbnail(url=event.guild.icon.url)
    embed.set_image(url=event.cover_image)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text = '\u200b', icon_url = "https://www.pngall.com/wp-content/uploads/5/Video-Game-Controller.png")
    await channel.send(embed=embed)


bot.run(os.getenv('DISCORD_BOT_TOKEN'))