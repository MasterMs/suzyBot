import json
import os
import datetime
import discord
import dotenv
import pymongo
from ui import Ui

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        dotenv.load_dotenv()
        self.db = pymongo.MongoClient(os.getenv("DB_CONNECT"))
        self.ui = Ui()
    
    async def on_ready(self):
        try:
            await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))
        except Exception as e:
            self.errorInvoked(e)

    async def on_message(self, message):
        try:
            await message.channel.send(self.guilds)
            await self.ui.response(message=message)
        except Exception as e:
            self.errorInvoked(e)

    def errorInvoked(self, e):
        self.db["SuzyData"]["errors"].insert_one({
                "date": datetime.utcnow(),
                "error": e
            })

