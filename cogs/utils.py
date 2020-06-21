import discord
from discord.ext import commands
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
import config

class Utils():
    def __init__(self):
        self.config = config

    async def checkOwner(self, ctx):
        if not self.config.owner_only:
            return True
            
        if ctx.author.id == self.config.owner_id:
            return True

        await ctx.send("**Sorry, you do not have permission to use this command, as the bot is on owner-only mode.**")
        return False