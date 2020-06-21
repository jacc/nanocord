import discord
import requests
from discord.ext import commands
import random
from discord import Webhook, RequestsWebhookAdapter, File
import json
from discord.ext.commands import has_permissions, MissingPermissions
from .utils import Utils


class Owner(commands.Cog, name="Owner Only Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def shutdown(self, ctx):
        """
        Shutdown bot.
        """
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))
