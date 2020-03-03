import json
import discord
import pymongo
import os
import json
import datetime

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.db = pymongo.MongoClient(os.getenv("DB_CONNECT"))
    
    async def on_ready(self):
        try:
            await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))
            return 0
        except Exception as e:
            self.errorInvoked(e)
            return 1
        
    async def on_message(self, message):
        try:
            if (any(s in message.content.lower() for s in ["-play", "-leave", "-stop"])) and (message.channel.id == 422450473304326147):
                await self.response(message, mode='g')
            elif any(s in message.content.lower() for s in self.db["SuzyData"]["Users"].find({"discordId": str(message.author.id).lower()})[0]["blacklist"]):
                await self.response(message, mode='b')
            return 0
        except Exception as e:
            self.errorInvoked(e)
            return 1

    async def response(self, message, mode=''):
        try:
            if mode == 'g':
                await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention}**')
            elif mode == 'b':
                await message.channel.send(f'<@{message.author.id}> **Hey! you can\'t say that word!**')
            else:
                pass
            await message.delete()
            return 0
        except Exception as e:
            self.errorInvoked(e)
            return 1

    def errorInvoked(self, error):
        self.db["SuzyData"]["errors"].insert_one({
                "date": datetime.datetime.utcnow(),
                "error": error
            })
