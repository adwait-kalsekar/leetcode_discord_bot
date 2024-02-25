import discord
from discord.ext import commands, tasks
import datetime
import main

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable member intents

# Create a Discord bot
bot = commands.Bot(intents=intents,command_prefix='$')

# Event: Bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # Start the scheduled task when the bot is ready
    my_background_task.start()

# Define the scheduled task
@tasks.loop(minutes=1)  # Run the task every 1 minute
async def my_background_task():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # Get the channel where you want to send the message (replace CHANNEL_ID)
    channel = bot.get_channel(1211005997976522785)
    # Send a message to the channel
    await channel.send(f'This is a scheduled message! Current time is {current_time}.')


async def send_reminder():
    print('Executing scheduled job...')

    channel = bot.get_channel(1211005997976522785)

    members = channel.members

    for member in members:
        print(member)

    # for user in users_list:
    #     date_string = user['created_at']
    #     date_time_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")

    #     current_time = datetime.utcnow()
    #     time_difference = current_time - date_time_object

    #     # twenty_four_hours = timedelta(days=1)

    #     # for Testing only
    #     five_minutes = timedelta(minutes=5)

    #     if time_difference > five_minutes:
    #         return True
    #     else: 
    #         return False
        
bot.run('MTIxMTAwNTIzMjgwOTY0ODEzOA.G-TRTg.oLLGEAclPvSbnimwJz6r6Pmer-m4CBp8zsTtBw')
