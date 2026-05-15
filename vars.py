

from os import environ

API_ID = int(environ.get("API_ID", "34422904"))
API_HASH = environ.get("API_HASH", "7e0002469784f47fc08a6b3d93d7ebed")
BOT_TOKEN = environ.get("BOT_TOKEN", "8753577119:AAFjtZO-PZtuDR93bA5_Ed3M-qUXbZDJmLM")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "Uploading5_bot")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/Uploading5_bot")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "5349573682"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://adarshppandey937:uIoPcln9vXQBF0vP@cluster0.o9mn6hb.mongodb.net/?")





