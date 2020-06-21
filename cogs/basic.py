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

    @commands.command()
    async def about(self, ctx):
        """
        Learn about the project!
        """
        embed = discord.Embed(title="Nanocord - About")
        embed.description = "Created by [@jacc](https://github.com/jacc), heavily inspired by [@venoras/Huecord](https://github.com/venoras/Huecord). \n\nCreated with :heart_decoration: in the USA (and under 2 hours!)\n\nAll rights reserved to the respective owners of copyrighted material, I don't know how legal stuff works but I don't own or claim to own the name Nanoleaf Auroras or Nanoleaf at all. If that's a problem contact me?"
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Essentials(bot))
