import json
import os
import datetime
import discord
import dotenv
from suzyDatabase import SuzyDatabase
from ui import Ui

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.db = SuzyDatabase(os.getenv("CONNECTION_STRING"))
        self.ui = Ui()

    async def on_ready(self):
        try:
            await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))
        except Exception as e:
            self.errorInvoked(e)

    async def on_message(self, message):
        try:
            await self.ui.response(message=message)
        except Exception as e:
            self.errorInvoked(e)

    def errorInvoked(self, e):
        self.db["Errors"].insert_one([{
                "date": datetime.datetime.utcnow(),
                "error": e
            }])

