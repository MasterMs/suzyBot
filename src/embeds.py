import discord

class Groovy(discord.Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Test'
        self.description = 'test'