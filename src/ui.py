import PyDictionary
import tenorpy

class Ui():
    def __init__(self) -> None:
        self.words = PyDictionary.PyDictionary()
        self.tenor = tenorpy.Tenor()

    async def response(self, message):
        if any(s in message.content.lower() for s in ["-play", "-leave", "-stop"]) and (message.channel.id in [422450473304326147, 690317486515814470]):
            await message.channel.send(f'<@{message.author.id}> **Hey! you can\'t say that word!**')
        elif message.content.lower()[0:4] == '-def':
            await message.channel.send(self.define(f"{message.content[5:]}"))
        elif message.channel.id == 727404164224778320:
            await message.add_reaction(self.get_emoji(690057068455264258))
            await message.add_reaction(self.get_emoji(727395835964424242))
            await message.add_reaction(self.get_emoji(743673927691272243))
        elif message.content.lower()[0:3] == '-gif':
            await message.channel.send(self.tenor.random(f'{message.content.lower()[4:]}'))
        elif message == "-members":
            await message.channel.send(message.guild)
        elif any(s in message.content.lower() for s in self.db["SuzyData"]["Users"].find({"discordId": str(message.author.id).lower()})[0]["blacklist"]):
            await message.channel.send(f'<@{message.author.id}> **Hey! you can\'t say that word!**')
    
    def define(self, word):
        defn = f"***{word.capitalize()}***\n"
        r = self.words.meaning(word)
        for i in r:
            for k in r[i]:
                defn += f'- {k}\n'
        return defn