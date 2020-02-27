import os
import dotenv
import pymongo
from suzyBot import SuzyBot

if __name__ == "__main__":
    try:
        client = pymongo.MongoClient(f'mongodb+srv://admin:{os.getenv("DB_PASSWORD")}@suzy-db-f4pio.mongodb.net/test?retryWrites=true&w=majority')
        db = client.test
        dotenv.load_dotenv()
        suzy = SuzyBot()
        suzy.run(os.getenv('DISCORD_TOKEN')) 
    except Exception as e:
        print(f"Error Encountered, Program Now Exiting\n{e}")
        exit()
