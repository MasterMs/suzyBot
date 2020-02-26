from utilities import Utilities
import json
import discord

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.userDict = {}
        self.commands = {
            '-play' : self.groovy_message
        }

    async def on_ready(self):
        self.printStartupDetails()
        self.readUsers()
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))

    async def groovy_message(self, message):
        print(f'Delete message {message.content}')
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
        await message.delete()

    async def on_message(self, message):
        try:
            await self.commands[message.content[0:5].lower()](message)
        except KeyError:
            pass
        except IndexError:
            pass
    
    def readUsers(self):
        with open('/usr/src/app/src/permissions.json', 'r') as userFile:
            users = json.load(userFile)
            for user in users:
                self.userDict[user['userId']] = user

    def printStartupDetails(self):
        Utilities.clear()
        print(f'Startup Details\n###################\n{self.user.name} has connected to {self.guilds[0].name}\nping: {int(self.latency*100)}ms')
