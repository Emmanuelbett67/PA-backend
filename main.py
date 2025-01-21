from bot.main_bot import TrackerBot
from config.config import BOT_TOKEN

if __name__ == "__main__":
    bot = TrackerBot(BOT_TOKEN)
    bot.run()
