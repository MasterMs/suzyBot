import os
import discord 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
game = discord.Game("Beating David | --help")


def botOut(string):
    if string == '--':
        return "**!!!!!!!!!هذا هو البادئة بوت تأخير**"
    elif string == '--help':
        return '*!!!!!!!!!!!!!!!!!!!!ما ، تحتاج إلى مساعدة ، لا مساعدة ، اللعنة عليك ، أنا سوزي*'
    else:
        return ".أنا عنصري."

@client.event
async def on_ready():
    print(f'\nStartup Details\n###################\n{client.user.name} has connected to {client.guilds[0].name}\nping: {str(client.latency*100)}ms')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    controlChars = ['-','!']
    if message.content[0:2] == '--':
        await message.channel.send(botOut(message.content))
    
    elif (message.content[0] in controlChars) and (message.channel.name == 'general'):
        print(f'Delete message {message.content}')
        await message.delete()
        await message.channel.send(f'<@{message.author.id}> **STOP SENDING BOT COMMANDS IN {message.channel.mention} ASSHOLE**')
    

if __name__ == "__main__":
    client.run(TOKEN) 

