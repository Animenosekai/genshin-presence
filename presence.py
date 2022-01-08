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
from nasse.logging import log

import current

START = time()

DISCORD_APPLICATION_ID = 929496938020208690  # Put your Discord Application ID

log(f"Connecting to Discord RPC with Application ID {DISCORD_APPLICATION_ID}")
RPC = Presence(str(DISCORD_APPLICATION_ID))
RPC.connect()

while True:
    log("Loading current settings")
    current = reload(current)
    log(f"Asking for the game data for UID {current.Player.HOYOLAB_UID}")
    user_data = get(
        f"https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard?uid={current.Player.HOYOLAB_UID}", headers={"Cookie": current.Settings.COOKIE}).json()
    for game_data in user_data["data"]["list"]:
        if current.Player.SERVER_REGION is not None and game_data["region"] != current.Player.SERVER_REGION.code:
            continue
        if game_data["game_id"] == current.Player.GAME.code:
            log(f"Found {current.Player.GAME} data for {game_data['region_name']}")
            log("Updating the RPC Client")
            RPC.update(
                state = f"{game_data['nickname']} 〜 Playing on {game_data['region_name']}",
                details = f"Currently at AR {game_data['level']}",
                large_image = current.Player.GAME.image,
                small_image = current.Player.CHARACTER.image,
                large_text = str(current.Text.TEXT),
                small_text = str(current.Text.CHARACTER_TEXT) if current.Text.CHARACTER_TEXT is not None else f"My favorite character is {current.Player.CHARACTER.name}",
                start = START
            )
            break
    log(f"Waiting for the next update ({current.Settings.REFRESH_RATE} seconds)")
    sleep(current.Settings.REFRESH_RATE + random())
