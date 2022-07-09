from datetime import datetime
from bot.dem import DemBot

dem_bot = DemBot()

if __name__ == "__main__":
    print(datetime.now())
    dem_bot.start()
