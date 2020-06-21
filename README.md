# Nanocord

### An extremely stupid solution to controlling your Nanoleaf products.

> Ever desired to allow your friends to control the lighting in your room via Discord? Have you ever wanted to change the color or effect on your Nanoleaf product in the middle of a game, but couldn't stop to open the app and change it? Nanocord eliminates all of that and allows anyone (or just you) to control your Nanoleafs straight from your favorite Discord server!

## Features

- Turn your Nanoleaf products on/off
- Set specific values for brightness, hue, and saturation
- List available effects
- Set to specific effect
- List information about the Nanoleaf product

## Dependencies

- [discord.py](https://github.com/Rapptz/discord.py)

## Setup

## Setup

1. Clone this repository: `git clone https://github.com/jacc/nanocord`

2. Run `pip3 install -r requirements.txt` to install all dependencies.

3. Modify the `config.example.py` with the relevant parameters, and rename it to `config.py`.

    1. Go to [Discord Developers](https://discord.com/developers) and create a **New Application**. Navigate to **Bot**, and click **Add Bot**. Paste the **token** into the configuration file.

    2. To find your **Discord User ID**, right click your profile and click **Copy ID**. Developer Mode must be enabled in `Settings -> Appearance`. Paste this ID into `owner_id` in the configuration file.

    3. To find your **Nanoleaf product IP address**, use the app or login to your router management panel. Nanoleaf products typically show up under ` IEEE Registration Authority` with a MAC address beginning with `00:55:DA`.
    
    4. Run `python3 get_auth_token.py` and follow the instructions to retrive your **Nanoleaf authorization token**, which is needed to authorize the bot.
    
    5. Input your **Nanoleaf product IP address** and **authorization token** into the proper fields.

4. To run the bot, use `python3 bot.py`.

## Configuration

- If you'd like the commands to be executable by any user, modify `owner_only` in `config.py` to `False`.
- If you'd like to log who uses each command, modify `logging` in `config.py` to `True`.
