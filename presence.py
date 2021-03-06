"""
presence.py

A Genshin Impact Discord RPC Presence script which gives your AR and additional information while playing.

https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard?uid=39079082
"""

from importlib import reload
from random import random
from time import sleep, time

from pypresence import Presence
from requests import get

import config

START = time()

DISCORD_APPLICATION_ID = 929496938020208690  # Put your Discord Application ID

print("Connecting to Discord RPC with Application ID {}".format(DISCORD_APPLICATION_ID))
RPC = Presence(str(DISCORD_APPLICATION_ID))
RPC.connect()

while True:
    print("Loading current settings")
    config = reload(config)
    print("Asking for the game data for UID {}".format(config.Player.HOYOLAB_UID))
    user_data = get("https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard?uid={}".format(config.Player.HOYOLAB_UID),
                    headers={"Cookie": config.Settings.COOKIE}).json()
    for game_data in user_data["data"]["list"]:
        if config.Player.SERVER_REGION is not None and game_data["region"] != config.Player.SERVER_REGION.code:
            continue
        if game_data["game_id"] == config.Player.GAME.code:
            print("Found {} data for {}".format(config.Player.GAME, game_data['region_name']))
            print("Updating the RPC Client")
            RPC.update(
                state="{} 〜 Playing on {}".format(game_data['nickname'], game_data['region_name']),
                details="Currently at AR {}".format(game_data['level']),
                large_image=config.Player.GAME.image,
                small_image=config.Player.CHARACTER.image,
                large_text=str(config.Text.TEXT),
                small_text=str(
                    config.Text.CHARACTER_TEXT) if config.Text.CHARACTER_TEXT is not None else f"My favorite character is {config.Player.CHARACTER.name}",
                start=START
            )
            break
    print("Waiting for the next update ({} seconds)".format(config.Settings.REFRESH_RATE))
    sleep(config.Settings.REFRESH_RATE + random())  # random is used to humanize a little bit the refresh rate
