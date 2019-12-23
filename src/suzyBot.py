from utilities import Utilities
import json

class SuzyBot:
    def __init__(self):
       self.users = {}

    def readUsers(self):
        with open('userProfile.json', 'r') as userFile:
            users = json.load(userFile)
            for user in users:
                self.users[user['userId']] = user

    def interp(self, string):
        if string == '--':
            return "**Suzy Bot Prefix**"
        elif string == '--help':
            return '''
            **Help**
            *--help*: Display Help for Bot
            *--refresh*: Update's user blacklist's from *userProfile.json*
            *--hadar*: Make Suzy yell in arabic
            '''
        elif string == '--refresh':
            self.readUsers()
        elif string == '--exit':
            Utilities.closeServer()
        elif string == '--hadar':
            return 'ديفيد أيها الأحمق الغبي ، لم أحبك أبداً ولن أفعل أبداً.'

    @staticmethod
    def printStartupDetails(client):
        Utilities.clear()
        print(f'Startup Details\n###################\n{client.user.name} has connected to {client.guilds[0].name}\nping: {int(client.latency*100)}ms')
