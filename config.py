import os

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

import asyncio



class Config:



ADMINS = [int(i) for i in os.environ.get("ADMIN", "1924628868 1481072635 1763070014 1481072635 1635614138 2107036689").split(" ")]
API_HASH = 72cbda887655ac7a5df871c87d8230cd
API_ID = 18402373
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5111412397:AAGBB0MZIPQkKcChqggQgfLUaQ3IarOJRJA")
CHANNELS = int(os.environ.get("CHANNELS", "-1001560241508"))
COLLECTION_NAME = Telegram_files
DATABASE_NAME = DhanushTG
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://dhanushtg:aaaa1111@cluster0.tcq8y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_CHANNEL = "-1001509130340"
PICS = "https://telegra.ph/file/fc3b31cdbfbe9fcf16cd9.mp4"
