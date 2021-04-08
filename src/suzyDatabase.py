import pymongo

class SuzyDatabase(pymongo.MongoClient):
    def __init__(self, host, port, document_class, tz_aware, connect, type_registry, **kwargs):
        super().__init__(host=host, port=port, document_class=document_class, tz_aware=tz_aware, connect=connect, type_registry=type_registry, **kwargs)
        
    def loadDatabase(self, guilds):
        for guild in guilds:        
            if self["Servers"].find({"serverId": guild.id}) != {}:
                self.db["Servers"].insert_one(guild.__dict__)