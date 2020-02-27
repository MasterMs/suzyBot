import json
import discord
import pymongo
import os
import json

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.suzySchema = pymongo.MongoClient(f"mongodb+srv://admin:{os.getenv('DB_PASSWORD')}@cluster-suzyschema-f4pio.azure.mongodb.net/test?retryWrites=true&w=majority")

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))

    async def groovy_message(self, message):
        print(f'Delete message {message.content}')
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
        await message.delete()

    async def on_message(self, message):
        try:
            if (message.content in self.suzySchema["SuzyData"]["Users"].find({"discordId": message.author.id})[0]["blackList"]):
                await message.delete()
            if (any(subString in message.content for subString in ["-play", "-leave"])) and (message.channel.id == 422450473304326147):
                await self.groovy_message(message)
        except KeyError:
            pass