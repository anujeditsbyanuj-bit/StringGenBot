from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN", "8694198519:AAHkfsd2hG584oC92jM-Ee2PJd2snDy49qM")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID",8931907813))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/anujedits97")
