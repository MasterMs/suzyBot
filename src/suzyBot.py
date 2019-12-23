from utilities import Utilities
import json

class SuzyBot:
    def __init__(self):
       self.users = {}

    def readUsers(self):
        with open('/Users/marco/suzyBot/src/userProfile.json', 'r') as userFile:
            for user in userFile:
                self.users['userId'] = user
    


    def interp(self, string):
        if string == '--':
            return "**Suzy Bot Prefix**"
        elif string == '--help':
            return '*Help\n--refresh: Update\'s user blacklist\'s from userProfile file\n*'
        elif string == '--refresh':
            self.readUsers()
        elif string == '--exit':
            Utilities.closeServer()

    @staticmethod
    def printStartupDetails(client):
        Utilities.clear()
        print(f'Startup Details\n###################\n{client.user.name} has connected to {client.guilds[0].name}\nping: {str(client.latency*100)}ms')

if __name__ == "__main__":
    x = SuzyBot()
    x.readUsers()
    print(x.users)

