from utilities import Utilities
import json
import discord

class SuzyBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.userDict = {}
        self.help = {
            '*--help*': "Display Help for Bot",
            '*--refresh*': "Update's user blacklist's from *userProfile.json*",
            '*--hadar*': 'Make Suzy yell in arabic'
            }

    async def on_ready(self):
        self.printStartupDetails()
        self.readUsers()
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))


    async def on_message(self, message):
        try:
            controlChars = ['-','!']
            if message.content[0:2] == '--':
                await message.channel.send(f'<@{message.author.id}>{self.interp(message.content)}')
                await message.delete()
            elif (message.content[0] in controlChars) and (message.channel.name == 'general'):
                print(f'Delete message {message.content}')
                await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
                await message.delete()
            elif message.content.lower() in self.userDict[message.author.id]['blacklist']:
                await message.delete()
        except KeyError:
            pass
        except IndexError:
            pass
    
    def readUsers(self):
        with open('D:/suzyBot/src/userProfile.json', 'r') as userFile:
            users = json.load(userFile)
            for user in users:
                self.userDict[user['userId']] = user

    def interp(self, string):
        if string == '--':
            return "**Suzy Bot Prefix**"
        elif string == '--help':
            helper = ''
            for i in self.userDict:
                helper.join([helper, i, self.userDict[i]])
            return helper
        elif string == '--refresh':
            self.readUsers()
            return " Blacklist refreshed"
        elif string == '--exit':
            Utilities.closeServer()
        elif string == '--hadar':
            return 'ديفيد أيها الأحمق الغبي ، لم أحبك أبداً ولن أفعل أبداً.'

    def printStartupDetails(self):
        Utilities.clear()
        print(f'Startup Details\n###################\n{self.user.name} has connected to {self.guilds[0].name}\nping: {int(self.latency*100)}ms')
