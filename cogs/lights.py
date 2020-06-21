import discord
import requests
from discord.ext import commands
import random
from discord import Webhook, RequestsWebhookAdapter, File
import json
from discord.ext.commands import has_permissions, MissingPermissions
from .utils import Utils

class Lights(commands.Cog, name="Lighting Commands"):
    def __init__(self, bot):
        self.bot = bot
        
    async def cog_check(self, ctx):
        return await Utils().checkOwner(ctx)
    
    @commands.command(pass_context=True)
    async def on(self, ctx):
        """
        Turn Nanoleaf Auroras on.
        """
        data = {
            "on": {
                "value": True
            }
        }

        headers = {
            "content-type": "application/json"
        }

        req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state', json=data, headers=headers)

        if req.status_code == 204:
            await ctx.send(":white_check_mark: Successfully turned on Nanoleaf Auroras.")
    
    @commands.command(pass_context=True)
    async def off(self, ctx):
        """
        Turn Nanoleaf Auroras off.
        """
        data = {
            "on": {
                "value": False
            }
        }

        headers = {
            "content-type": "application/json"
        }
        req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state', json=data, headers=headers)

        if req.status_code == 204:
            await ctx.send(":white_check_mark: Successfully turned off Nanoleaf Auroras.")

    @commands.command(pass_context=True)
    async def brightness(self, ctx, *args):
        """
        Get current brightness or set brightness.
        """
        if args:
            data = {"brightness" : {"value":int(args[0])}}

            headers = {
                "content-type": "application/json"
            }
            req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state', json=data, headers=headers)

            if req.status_code == 204:
                await ctx.send(f":white_check_mark: Set brightness to `{args[0]}%`.")
        else:
            req = requests.get(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state/brightness')
            
            await ctx.send(f':high_brightness: Brightness is currently set to `{req.json()["value"]}%`.')
    
    @commands.command(pass_context=True)
    async def hue(self, ctx, *args):
        """
        Get current hue or set hue.
        """
        if args:
            data = {"hue" : {"value":int(args[0])}}

            headers = {
                "content-type": "application/json"
            }
            req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state', json=data, headers=headers)

            if req.status_code == 204:
                await ctx.send(f":white_check_mark: Set hue to `{args[0]}`.")
        else:
            req = requests.get(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state/hue')
            
            await ctx.send(f':high_brightness: Hue is currently set to `{req.json()["value"]}`.')
    
    @commands.command(pass_context=True)
    async def saturation(self, ctx, *args):
        """
        Get current saturation or set saturation.
        """
        if args:
            data = {"sat" : {"value":int(args[0])}}

            headers = {
                "content-type": "application/json"
            }
            req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state', json=data, headers=headers)

            if req.status_code == 204:
                await ctx.send(f":white_check_mark: Set saturation to `{args[0]}`.")
        else:
            req = requests.get(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/state/sat')
            
            await ctx.send(f':high_brightness: Saturation is currently set to `{req.json()["value"]}`.')
    
    @commands.command(pass_context=True)
    async def listeffects(self, ctx):
        """
        Get list of available effects.
        """
        req = requests.get(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/effects/effectsList')

        if req.status_code == 200:

            json = req.json()

            formatted = ""

            for i in json:
                formatted += f"- {i}\n" 

            await ctx.send(embed=discord.Embed(title="Available Effects", description=formatted))

    @commands.command(pass_context=True)
    async def seteffect(self, ctx, *, args):
        """
        Set effect on the Auroras.
        """
        data = {"select": args}

        headers = {
            "content-type": "application/json"
        }

        req = requests.put(f'http://{self.bot.config.aurora_ip}:16021/api/v1/{self.bot.config.aurora_auth}/effects', json=data, headers=headers)

        if req.status_code == 204:
            await ctx.send(f":milky_way: Successfully set effect to {args}")
        else:
            await ctx.send(f":x: Couldn't find an effect by that name. Check your spelling and try again.")






def setup(bot):
    bot.add_cog(Lights(bot))
