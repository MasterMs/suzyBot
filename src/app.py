import os
import discord 
from dotenv import load_dotenv
from utilities import Utilities
from suzyBot import SuzyBot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
game = discord.Game("Beating David | --help")

@client.event
async def on_ready():
    SuzyBot.printStartupDetails(client)    
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    controlChars = ['-','!']
    print(message.content[0:2])
    if message.content[0:2] == '--':
        await message.channel.send(SuzyBot.interpHelp(message.content))
        await message.delete()
    elif (message.content[0] in controlChars) and (message.channel.name == 'general'):
        print(f'Delete message {message.content}')
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
        await message.delete()

    

if __name__ == "__main__":
    client.run(TOKEN) 

