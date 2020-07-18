import json
import os
import datetime
import discord
import dotenv
import pymongo
import urbandictionary as ud
from PyDictionary import PyDictionary

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        dotenv.load_dotenv()
        self.db = pymongo.MongoClient(os.getenv("DB_CONNECT"))
        self.words = PyDictionary()
    
    async def on_ready(self):
        try:
            await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))
        except Exception as e:
            self.errorInvoked(e)
    
    async def on_message(self, message):
        try:
            if any(s in message.content.lower() for s in ["-play", "-leave", "-stop"]) and (message.channel.id == 422450473304326147):
                await self.response(message, mode='g')
            elif any(s in message.content.lower() for s in self.db["SuzyData"]["Users"].find({"discordId": str(message.author.id).lower()})[0]["blacklist"]):
                await self.response(message, mode='b')
            elif message.content.lower()[0:4] == '-def':
                await message.channel.send(embed=self.define(message.content[5:]))
            elif message.channel.id == 727404164224778320:
                await message.add_reaction(self.get_emoji(690057068455264258))
                await message.add_reaction(self.get_emoji(727395835964424242))
        except Exception as e:
            self.errorInvoked(e)

    def define(self, word):
        try:
            defn = self.words.meaning(word)
            if defn == {} or None:
                defn = str(ud.define(word))

            embd = discord.Embed(title="SuzyBot", description="Dictionary")
            embd.add_field(name="definition", value=defn[str(word).lower()])
            return embd
        except Exception as e:
            self.errorInvoked(e)

    async def response(self, message, mode=''):
        try:
            if mode == 'g':
                await message.channel.send(f'<@{message.author.id}> **STOP SENDING GROOVY COMMANDS IN {message.channel.mention}**')
            elif mode == 'b':
                await message.channel.send(f'<@{message.author.id}> **Hey! you can\'t say that word!**')
            else:
                pass
            await message.delete()
        except Exception as e:
            self.errorInvoked(e)

    def errorInvoked(self, error):
        print(error)
        # self.db["SuzyData"]["errors"].insert_one({
        #         "date": datetime.datetime.utcnow(),
        #         "error": error
        #     })