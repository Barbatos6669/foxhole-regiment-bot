import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import logging.handlers
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

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

@bot.event
async def on_ready():
    logger.info(f'We have logged in as {bot.user}')
    print(discord.__version__)

async def main():
    try:
        await bot.load_extension('cogs.hello_cog')
    except Exception as e:
        logger.error(f"Failed to load extension 'bot.cogs.hello_cog': {e}", exc_info=True)
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())