import discord, requests, random, config
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter, File
from discord.ext.commands import has_permissions, MissingPermissions
import datetime

bot = commands.Bot(command_prefix=config.prefix)

bot.config = config


@bot.event
async def on_ready():
    bot.remove_command("help")
    for cog in config.cogs:
        bot.load_extension(cog)


@bot.event
async def on_command(ctx):
    if config.logging == True:
        print(f"[{datetime.datetime.now()}] {ctx.author} used {ctx.command}")
    else:
        pass


if __name__ == "__main__":
    try:
        req = requests.get(
            f"http://{config.aurora_ip}:16021/api/v1/{config.aurora_auth}"
        )
        json = req.json()
        if json["name"]:
            bot.deviceName = json["name"]
            print(
                f"✅ {json['name']} (version {json['firmwareVersion']}) on {config.aurora_ip} successfully connected."
            )
            print(
                f"\nCreated by Jack LaFond (@jacc on GitHub)\n-- Special Thanks:\n- @venoras/Huecord\n- @software-2/nanoleaf\n\nAny issues? Feel free to open an issue on the GitHub repository. PRs are welcomed!"
            )
            bot.run(config.token)
    except Exception as e:
        print(
            "I couldn't find any panels with that IP / the pairing code was incorrect! Double check the config values and try again."
        )
