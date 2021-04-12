import pymongo
from pymongo import mongo_client

class SuzyDatabase(mongo_client):
    def __init__(self, connection="") -> None:
        super().__init__(connection=connection)

    def loadDatabase(self, guilds):
        for guild in guilds:        
            if self["Servers"].find({"serverId": guild.id}) != {}:
                self["Servers"].insert_one(guild.__dict__)
        

