import os
import dotenv
from suzyBot import SuzyBot

if __name__ == "__main__":
    try:
        dotenv.load_dotenv()
        suzy = SuzyBot()
        suzy.run(os.getenv('DISCORD_TOKEN')) 
    except:
        print("Error Encountered, Program Now Exiting")
        exit()
