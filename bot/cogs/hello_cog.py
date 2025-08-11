from discord.ext import commands
# Slash commands

class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Loaded {self.__class__.__name__} successfully.")


async def setup(bot):
    await bot.add_cog(HelloCog(bot))
