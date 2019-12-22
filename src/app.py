import os
import discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to the server')

@client.event
async def on_message(message):
    commands = ['-play', '-PLAY', '-stop', '-STOP', '-skip', '-SKIP']
    if (message.content in commands) and (message.channel.name == 'general'):
        print(f'Delete message {message.content}')
        await message.delete()
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')

client.run(TOKEN) 