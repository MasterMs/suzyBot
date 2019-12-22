import os
import discord 
import json
from dotenv import load_dotenv
from utilities import Utilities
from suzyBot import SuzyBot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
suzy = SuzyBot()
               

@client.event
async def on_ready():
    SuzyBot.printStartupDetails(client)
    suzy.readUsers()
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Beating David | --help"))

@client.event
async def on_message(message):
    controlChars = ['-','!']
    suzy.checkDel()
    if message.content[0:2] == '--':
        await message.channel.send(f'<@{message.author.id}>{suzy.interp(message.content)}')
        await message.delete()
    elif (message.content[0] in controlChars) and (message.channel.name == 'general'):
        print(f'Delete message {message.content}')
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
        await message.delete()
    elif message.content in suzy.users[message.author.id]['words']:
            message.delete()


if __name__ == "__main__":
    client.run(TOKEN) 

