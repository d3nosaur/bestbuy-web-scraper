import discord
import asyncio
import random
from scraper import product_available
from config import config
from config import discord_config

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

async def message_user(userID, message):
    user = client.get_user(userID)

    if(user == None):
        print("ERR: Can not find a discord user by that tag")
        return False

    try:
        await user.send(message)
    except discord.Forbidden:
        print("ERR: Bot does not have permission to send a message to this user.")
        return False
    else:
        return True

async def check_availability():
    print("Starting Discord Scraper Cycle")
    while True:
        available = product_available(config["url"], config["headers"])

        if True:
            print("The item is available")
            message = await message_user(discord_config["ping_user_id"], "The scraper item is available.")
            if(message == False):
                return False
        
        await asyncio.sleep(config["delay"] + (random.randint(1,100)/100))

@client.event
async def on_ready():
    print("Connected to Discord")
    asyncio.ensure_future(check_availability())

def start_bot():
    print("Starting the Discord Bot")
    client.run(discord_config["bot_token"])