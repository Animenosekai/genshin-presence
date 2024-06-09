"""
presence.py

A Genshin Impact Discord RPC Presence script which gives your AR and additional information while playing.
"""
import dataclasses
import importlib
import os
import random
import threading
import time
import types
import typing
import pathlib

import nasse
import pypresence
import requests
import rich.progress
from assets import characters, games, regions
from nasse.utils.formatter import format


@dataclasses.dataclass
class GameData:
    game: games.Game
    """The game"""
    region: str
    """The region the player is playing in"""
    name: str
    """The name of the player"""
    level: int
    """The level of the player (ex: Adventure Rank on Genshin)"""

class GenshinPresence:
    """
    The Genshin Impact Discord RPC Presence

    It can connect to the Discord RPC and show the player's information while playing Genshin Impact
    """

    def __init__(self, config: types.ModuleType) -> None:
        """
        Initializes the presence

        Parameters
        ----------
        config: module
        """
        self.config = config
        "The configuration file"
        self.rpc = self.connect(self.config.Settings.DISCORD_APPLICATION_ID)
        "The Discord RPC Client"
        self.start = time.time()
        "The start time of the presence"
        nasse_config = nasse.NasseConfig(name=self.__class__.__name__)
        self.logger = nasse.Logger(nasse_config)
        "The logger instance"
        self._runs: typing.Dict[typing.Tuple[int, int], bool] = {}
        "The (PID, THREAD_ID) -> RUNNING mapping"

    def connect(self, application_id: int) -> pypresence.Presence:
        """
        Connects to the Discord RPC

        Parameters
        ----------
        application_id: int
            The Discord Application ID

        Returns
        -------
        Presence
            The Discord RPC Client
        """
        RPC = pypresence.Presence(str(self.config.Settings.DISCORD_APPLICATION_ID))
        RPC.connect()
        return RPC

    def reset_start(self) -> None:
        """Resets the start time"""
        self.start = time.time()

    def reload_config(self) -> None:
        """Reloads the configuration file"""
        self.config = importlib.reload(self.config)

    def retrieve_cookie(self) -> str:
        """
        Retrieves the cookie from the configuration file

        Returns
        -------
        str
            The cookie
        """
        result = ""
        if self.config.Settings.COOKIE:
            result = self.config.Settings.COOKIE
            result = str(result).strip()
        if not result and "COOKIE" in os.environ:
            result = os.environ["COOKIE"]
            result = str(result).strip()
        path = pathlib.Path(__file__).parent / "COOKIE"
        if not result and path.is_file():
            result = path.read_text().strip()
        if not result:
            raise ValueError("No cookie found")
        return result

    def get_game_data(self, hoyolab_uid: int) -> GameData:
        """
        Gets the game data from the HoYoLAB API

        Parameters
        ----------
        hoyolab_uid: int

        Returns
        -------
        GameData
            The game data associated with the player

        Raises
        ------
        ValueError
            When no game data is found
        """
        try:
            cookie = self.retrieve_cookie()
        except ValueError:
            self.logger.warn("Couldn't find the cookie in the configuration file")
            cookie = ""
        request = requests.get(
            "https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard",
            headers={"Cookie": cookie},
            params={"uid": hoyolab_uid},
        )
        request.raise_for_status()
        user_data = request.json()
        if not user_data:
            raise ValueError("No data found")
        if "data" not in user_data:
            raise ValueError("No `data` found")
        if "list" not in user_data["data"]:
            raise ValueError("No `data.list` found")
        for game_data in user_data["data"]["list"]:
            if (
                self.config.Player.SERVER_REGION is not None
                and game_data["region"] != self.config.Player.SERVER_REGION.code
            ):
                continue
            if game_data["game_id"] == self.config.Player.GAME.code:
                return GameData(
                    game=self.config.Player.GAME,
                    region=game_data["region_name"],
                    name=game_data["nickname"],
                    level=game_data["level"],
                )
        raise ValueError("No game data found")

    def sleep(self, amount: typing.Optional[typing.Union[int, float]] = None) -> float:
        """
        Sleeps for a random amount of time between `time` and `time` + 1 second

        Parameters
        ----------
        amount: NoneType | float | int, default = None
        time: NoneType | float | int, default = None
            The time to sleep for. If None, it will sleep for the refresh rate specified in the configuration

        Returns
        -------
        float
        """
        amount = amount if amount is not None else self.config.Settings.REFRESH_RATE
        sleep_time = amount + random.random()
        time.sleep(sleep_time)
        return sleep_time

    def update_rpc(self, game_data: GameData) -> None:
        """
        Updates the Discord RPC Client with the game data

        Parameters
        ----------
        game_data: GameData
            The game data to update the RPC with
        """
        format_data = {
            "name": game_data.name,
            "region": game_data.region,
            "level": game_data.level,
            "character": self.config.Player.CHARACTER.name,
            "game": self.config.Player.GAME.name,
        }
        self.rpc.update(
            state=format(self.config.Text.STATE_TEXT, **format_data),
            details=format(self.config.Text.DETAILS_TEXT, **format_data),
            large_image=self.config.Player.GAME.image,
            small_image=self.config.Player.CHARACTER.image,
            large_text=format(self.config.Text.HOVER_TEXT, **format_data),
            small_text=format(self.config.Text.HOVER_CHARACTER_TEXT, **format_data),
            start=self.start,
        )

    def run(self) -> None:
        """
        Runs the presence in a loop
        
        Warning: This method is blocking
        """
        # Avoid overlapping with other instances if ran in another thread
        pid, tid = (os.getpid(), threading.get_ident())
        self._runs[pid, tid] = True
        self.logger.print(
            "[PID: {pid}] [TID: {tid}] Connecting to Discord RPC with Application ID `{aid}`".format(
                pid=pid, tid=tid, aid=self.config.Settings.DISCORD_APPLICATION_ID
            )
        )
        with rich.progress.Progress(
            *(
                rich.progress.TextColumn("[progress.description]{task.description}"),
                rich.progress.TextColumn("—"),
                rich.progress.TimeElapsedColumn(),
            ),
            transient=True
        ) as progress:
            task = progress.add_task(
                description="🍡 Launching {class_name} for HoYoLAB UID {uid}".format(
                    class_name=self.__class__.__name__,
                    uid=self.config.Player.HOYOLAB_UID,
                )
            )
            self.logger._rich_console = progress.console
            while self._runs[pid, tid]:
                game_data = self.flow()
                if game_data:
                    progress.update(
                        task,
                        description="🍡 {name} is playing {game} (AR {level})".format(
                            name=game_data.name,
                            game=game_data.game.name,
                            level=game_data.level,
                        ),
                    )
                slept = self.sleep()
                self.logger.print("Slept for {} seconds".format(slept))
            self.logger.print(
                "[PID: {pid}] [TID: {tid}] Stopped the presence".format(
                    pid=pid, tid=tid
                )
            )

    def stop(
        self, pid: typing.Optional[int] = None, tid: typing.Optional[int] = None
    ) -> None:
        """
        Stops the presence

        Parameters
        ----------
        pid: NoneType | int, default = None
        tid: NoneType | int, default = None
        """
        pid = pid if pid is not None else os.getpid()
        tid = tid if tid is not None else threading.get_ident()
        self._runs[pid, tid] = False
        self.logger.print(
            "[PID: {pid}] [TID: {tid}] Requested stop for the presence".format(
                pid=pid, tid=tid
            )
        )

    def flow(self) -> typing.Optional[GameData]:
        """
        The main flow of the presence

        Returns
        -------
        ForwardRef('GameData')
        NoneType
        GameData
        """
        self.logger.print("Reloading settings")
        self.reload_config()
        self.logger.print(
            "Asking for the game data for UID `{}`".format(
                self.config.Player.HOYOLAB_UID
            )
        )
        try:
            game_data = self.get_game_data(hoyolab_uid=self.config.Player.HOYOLAB_UID)
        except ValueError:
            self.logger.print("No game data found")
            return None
        self.logger.print(
            "Found `{}` data for `{}`".format(
                self.config.Player.GAME.name, game_data.region
            )
        )
        self.logger.print("Updating the RPC Client")
        self.update_rpc(game_data)
        self.logger.print(
            "Waiting for the next update ({} seconds)".format(
                self.config.Settings.REFRESH_RATE
            )
        )
        return game_data


if __name__ == "__main__":
    import config

    presence = GenshinPresence(config=config)
    presence.run()

