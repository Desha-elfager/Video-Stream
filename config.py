import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "DESHA_MUSIC1_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "music_Desha")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "music_Desha1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a1617bd434b68b3dcedb7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Desha-elfager/VC_DESHA_2022")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a1617bd434b68b3dcedb7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a1617bd434b68b3dcedb7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f2c7e2753673bd1ee134a.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/627ccc08b20f992539174.jpg")
