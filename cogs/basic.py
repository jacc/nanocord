import discord
import requests
from discord.ext import commands
import random
from discord import Webhook, RequestsWebhookAdapter, File
import json
from discord.ext.commands import has_permissions, MissingPermissions
from cogs.utils import Utils


class Essentials(commands.Cog, name="Essential Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """
        Get bot latency.
        """
        await Utils().sendEmbed(
            ctx, description=f":ping_pong: `{round(self.bot.latency * 1000, 1)}ms`",
        )

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """
        Get command information.
        """
        embed = discord.Embed()
        for el in self.bot.cogs:
            sub = self.bot.get_cog(el)
            formatted = ""
            for x in sub.get_commands():
                formatted += f"{x.name}, "
            if formatted == "":
                pass
            else:
                embed.add_field(
                    name=sub.qualified_name, value=formatted[:-2], inline=False
                )
        await ctx.send(embed=embed)

    @commands.command()
    async def about(self, ctx):
        """
        Learn about the project!
        """
        await Utils().sendEmbed(
            ctx,
            title="Nanocord - About",
            description="Created by [@jacc](https://github.com/jacc), heavily inspired by [@venoras/Huecord](https://github.com/venoras/Huecord). \n\nCreated with :heart_decoration: in the USA (and under 4 hours!)\n\nAll rights reserved to the respective owners of copyrighted material, I don't know how legal stuff works but I don't own or claim to own the name Nanoleaf Auroras or Nanoleaf at all. If that's a problem contact me?",
        )


def setup(bot):
    bot.add_cog(Essentials(bot))
