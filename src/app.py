import os
from suzyBot import SuzyBot

if __name__ == "__main__":
    try:
        suzy = SuzyBot()
        suzy.run(os.getenv('DISCORD_TOKEN'))
    except Exception as e:
        print(f"{e}\nError Encountered, Program Now Exiting")
        exit()
