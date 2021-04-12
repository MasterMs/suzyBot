import pymongo
from pymongo import mongo_client

class SuzyDatabase(pymongo.MongoClient):
    def __init__(self, connect) -> None:
        return super().__init__(connect=connect)

    def loadDatabase(self, guilds):
        for guild in guilds:        
            if self["Servers"].find({"serverId": guild.id}) != {}:
                self["Servers"].insert_one(guild.__dict__)
        
    