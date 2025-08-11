import os
from discord.ext import commands
import discord
import json
import logging
import errno

class SetupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.default_channel_data = {
            "logs": 0,
            "general": 0
        }
        self.logger = logging.getLogger


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Loaded {self.__class__.__name__} successfully.")

        # Check if the configs folder exists
        if not os.path.exists("configs"):
            print("configs folder not found.")
            try:
                os.makedirs("configs")
                print("configs folder created.")
            except Exception as e:
                print(f"Failed to create configs folder: {e}")
        else:
            print("configs folder found.")

        # Check if the default channels config exists
        if not os.path.exists("configs/default_channels.json"):
            print("Default channels config not found.")
            try:
                with open("configs/default_channels.json", "w") as f:
                    json.dump(self.default_channel_data, f)
                print("Default channels config created.")
            except Exception as e:
                print(f"Failed to create default channels config: {e}")
        else:
            print("Default channels config found.")

async def setup(bot):
    await bot.add_cog(SetupCog(bot))