import discord
import requests
from discord.ext import commands
import random
from discord import Webhook, RequestsWebhookAdapter, File
import json
from discord.ext.commands import has_permissions, MissingPermissions
from .utils import Utils


class Manage(commands.Cog, name="Management Commands"):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await Utils().checkOwner(ctx)

    @commands.command(pass_context=True)
    async def identify(self, ctx):
        """
        Identify Nanoleaf panels.
        """
        try:
            req = requests.put(
                f"http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/identify"
            )
            if req.status_code == 200:
                await Utils().sendEmbed(
                    ctx,
                    description=f"Your **{self.bot.deviceName}** are connected and should be flashing green!",
                )
        except Exception as e:
            await Utils().sendEmbed(
                ctx,
                description=f"Are you sure that your Nanoleaf product is connected and you're on the same Wifi network? Double check your configuration and try again.",
            )

    @commands.command(pass_context=True)
    async def info(self, ctx):
        """
        Get information about your Nanoleaf Aurora panels.
        """
        req = requests.get(
            f"http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}"
        )
        json = req.json()

        embed = discord.Embed(title=json["name"])
        embed.description = f":id: Serial #: `{json['serialNo']}`\n:robot: Firmware Version: `{json['firmwareVersion']}`"
        embed.add_field(
            name=":1234: # of panels", value=json["panelLayout"]["layout"]["numPanels"]
        )
        embed.add_field(
            name=":1234: # of effects", value=len(json["effects"]["effectsList"])
        )
        embed.add_field(
            name=":bulb: Currently on?",
            value=f"{'No' if json['state']['on']['value'] == False else 'Yes'}",
        )
        embed.add_field(
            name=":milky_way: Current Effect", value=json["effects"]["select"]
        )
        embed.add_field(
            name=":high_brightness: Brightness",
            value=f"{json['state']['brightness']['value']}%",
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Manage(bot))
