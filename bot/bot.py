import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import logging
import logging.handlers
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Intents 
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.presences = True

# Bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}\n', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Events
@bot.event
async def on_ready():
    logger.info(f'We have logged in as {bot.user}')
    print(f'Discord.py version: {discord.__version__}')
    print(f'Bot ID: {bot.user.id}')
    print(f'Bot Username: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        logger.error(f'Failed to sync commands: {e}', exc_info=True)

# Load Cogs
async def main():
    try:
        await bot.load_extension('cogs.setup_cog')
    except Exception as e:
        logger.error(f"Failed to load extension 'cogs.setup_cog': {e}", exc_info=True)
        print(f"Failed to load extension 'cogs.setup_cog': {e}")  
    try:
        await bot.load_extension('cogs.hello_cog')        
    except Exception as e:
        logger.error(f"Failed to load extension 'cogs.hello_cog': {e}", exc_info=True)
        print(f"Failed to load extension 'cogs.hello_cog': {e}")
    await bot.start(TOKEN)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())