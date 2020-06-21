token = "your bot token"  # Get this from https://discord.com/developers
cogs = [
    "cogs.basic",
    "cogs.lights",
    "cogs.manage",
    "cogs.owner",
]  # Don't touch this unless you have good reason
prefix = "nano "  # Bot prefix
owner_id = 657057112593268756  # your Discord user ID, turn on Developer Mode in Settings, right click your name and click copy ID
owner_only = (
    True  # True for only you to use the commands, False if you want your friends to
)
logging = True  # Log who uses the bot commands
aurora_ip = "192.168.1.2"  # Your Nanoleaf product IP address
aurora_auth = (
    "WOaC1WnOp2aNlfleK1GfaNtHbtL9m896"  # Obtained from using get_auth_token.py
)

