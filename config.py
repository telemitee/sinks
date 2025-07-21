import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7869629794:AAH7sk6TXq2Gye-Vi0nGzX_ZOxQM4EeocqM")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "21184495"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "7238819d51a5280143fc3023a2f1abed")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002617085129"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "7527170018"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "https://t.me/")

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://akashz9t:akash123@cluster0.zu0io.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DB_NAME = os.environ.get("DATABASE_NAME", "heavy")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/JP6.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
