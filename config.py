#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7740749465:AAFRkcAa7VfgudR7YmfX2D18v-rD1xwAMyM")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22706444"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6e835a092d3431effe2c909873db1dab")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002478741954"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Fushiguro_x")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5961139833"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sanji01:sanji01@sanjimongo02.zgs4i.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Castlevania_Movie_File_Store_Bot")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002156718981"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002185767677"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/IiE.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/IiF.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀ ᴍᴏᴠɪᴇs ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Movies_Castlevania ...\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Movies_Castlevania>𝐅ᴜsʜɪɢᴜʀᴏ 𝐒ᴀᴍᴀ</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Fushiguro_x>𝐅ᴜsʜɪɢᴜʀᴏ 𝐒ᴀᴍᴀ</a>\n◈ ᴍᴇᴍʙᴇʀ ᴏꜰ : <a href=https://t.me/Straw_Hat_Bots>𝐒ᴛʀᴀᴡ 𝐇ᴀᴛ 𝐁ᴏᴛs</a>\n◈ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Movies_Castlevania>𝐌ᴏᴠɪᴇs 𝐂ᴀsᴛʟᴇᴠᴀɴɪᴀ</a>\n◈ ʜɪɴᴅɪ sᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/anime_flux>𝐀ɴɪᴍᴇ 𝐅ʟᴜx</a>\n◈ ʜɪɴᴅɪ ᴅᴜʙ ᴀɴɪᴍᴇ : <a href=https://t.me/Anime_Multiverse_Hindi>𝐂ʀᴜɴᴄʜʏʀᴏʟʟ</a>\n◈ ʜᴇᴍᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Adult_Flux>𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Straw_Hat_Bots>𝐅ᴜsʜɪɢᴜʀᴏ 𝐒ᴀᴍᴀ</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>𝐇ᴇʟʟᴏ!! {mention}⚡,\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Movies_Castlevania'>𝐌ᴏᴠɪᴇs 𝐂ᴀsᴛʟᴇᴠᴀɴɪᴀ</a></b>")
try:
    ADMINS=[6727550037]
    for x in (os.environ.get("ADMINS", "6727550037 7263364323 1683225887").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝐇ᴇʟʟᴏ !! {mention}✨,\n\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ • ᴛʀʏ ᴀɢᴀɪɴ • ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ᴍᴏᴠɪᴇ ꜰɪʟᴇ.\n\n𝐌ᴀɪɴ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Movies_Castlevania'>𝐌ᴏᴠɪᴇs 𝐂ᴀsᴛʟᴇᴠᴀɴɪᴀ</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝐂ʜᴜᴛɪʏᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴏᴡɴᴇʀ!!\n\nᴍʏ ᴏᴡɴᴇʀ : @Movies_Castlevania ..."

ADMINS.append(OWNER_ID)
ADMINS.append(5961139833)

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
   
