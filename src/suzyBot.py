from utilities import Utilities

class SuzyBot:
    @staticmethod
    def interpHelp(string):
        if string == '--':
            return "**!!!!!!!!!هذا هو البادئة بوت تأخير**"
        elif string == '--help':
            return '*!!!!!!!!!!!!!!!!!!!!ما ، تحتاج إلى مساعدة ، لا مساعدة ، اللعنة عليك ، أنا سوزي*'
        elif string == '--exit':
            Utilities.closeServer()

    @staticmethod
    def printStartupDetails(client):
        Utilities.clear()
        print(f'Startup Details\n###################\n{client.user.name} has connected to {client.guilds[0].name}\nping: {str(client.latency*100)}ms')