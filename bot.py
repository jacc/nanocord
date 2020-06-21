import discord, requests, random, config
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter, File
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix=config.prefix)

bot.config = config

@bot.event
async def on_ready():
    for cog in config.cogs:
        bot.load_extension(cog)
    
    print("\nWelcome to Nanocord! I'm going to try to connect to your Nanoleaf Aurora panels that you've specified in your config.")

    req = requests.get(f'http://{config.aurora_ip}:16021/api/v1/{config.aurora_auth}')
    json = req.json()
    if json['name']:
        print(f"Nanoleaf Auroras found! I see {json['name']} with a firmware version of {json['firmwareVersion']} and a serial number of {json['serialNo']}.\nIf these panels are the incorrect ones, double check the IP you specified in the console. Elsewise, enjoy the bot!\n\nCreated by Jack LaFond (@jacc on GitHub)\n-- Special Thanks:\n- @venoras/Huecord\n\nAny issues? Feel free to open an issue on the GitHub repository. PRs are welcomed!")
    else:
        print("I couldn't find any panels with that IP! Double check the config and try again.")
if __name__ == "__main__":
    bot.run(config.token)
