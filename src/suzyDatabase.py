import pymongo
from pymongo import mongo_client

class SuzyDatabase(pymongo.MongoClient):
    def __init__(self, host=None, port=None, document_class=None, tz_aware=None, connect=None, type_registry=None, **kwargs):
        super().__init__(host=host, port=port, document_class=document_class, tz_aware=tz_aware, connect=connect, type_registry=type_registry, **kwargs)

    def loadDatabase(self, guilds):
        for guild in guilds:        
            if self["Servers"].find({"serverId": guild.id}) != {}:
                self["Servers"].insert_one(guild.__dict__)
        

