import os
import discord 
import json
from dotenv import load_dotenv
from utilities import Utilities
from suzyBot import SuzyBot

if __name__ == "__main__":
    try:
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')
        suzy = SuzyBot()
        suzy.run(TOKEN) 
    except:
        print("Error Encountered, Program Now Exiting")
        exit()
