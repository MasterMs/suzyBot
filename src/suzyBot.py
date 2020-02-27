import json
import discord
import pymongo
import os
import json
import datetime

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.db = pymongo.MongoClient(f"mongodb+srv://admin:{os.getenv('DB_PASSWORD')}@cluster-suzyschema-f4pio.azure.mongodb.net/test?retryWrites=true&w=majority")
    
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))

    async def on_message(self, message):
        try:
            if (any(s in message.content.lower() for s in ["-play", "-leave"])) and (message.channel.id == 422450473304326147):
                await self.response(message, mode='g')
            elif any(s in message.content.lower() for s in self.db["SuzyData"]["Users"].find({"discordId": str(message.author.id).lower()})[0]["blacklist"]):
                await self.response(message, mode='b')
        except IndexError as e:
            self.db["SuzyData"]["errors"].insert({
                "date": datetime.datetime.utcnow(),
                "error": e
            })

    async def response(self, message, mode=''):
        if mode == 'g':
            await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
        elif mode == 'b':
            await message.channel.send(f'<@{message.author.id}> **Hey! you can\'t say that word! ASSHOLE**')
        else:
            pass
        await message.delete()