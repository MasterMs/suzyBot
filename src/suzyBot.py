import os
import discord
from suzyDatabase import SuzyDatabase
from ui import Ui

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.db = SuzyDatabase(connect=os.getenv("DB_CONNECT"))
        self.ui = Ui()

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))

    async def on_message(self, message):
        await self.ui.response(message=message)

