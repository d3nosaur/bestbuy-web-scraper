from discord_integration import start_bot
from config import config
from config import discord_config

def main():
    if(discord_config["enabled"]):
        start_bot()

if __name__ == "__main__":
    print("Starting the scrapper bot")
    main()