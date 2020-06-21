import discord
import requests
from discord.ext import commands
import random
from discord import Webhook, RequestsWebhookAdapter, File
import json
from discord.ext.commands import has_permissions, MissingPermissions

class Essentials(commands.Cog, name="Essential Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Get bot latency.
        """
        m = await ctx.send(
            f":satellite_orbital: `{round(self.bot.latency * 1000, 1)}ms`"
        )
        
def setup(bot):
    bot.add_cog(Essentials(bot))
