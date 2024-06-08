import typing
import dataclasses

from assets import characters, games, regions


@dataclasses.dataclass
class Player:
    GAME: games.Game = games.GENSHIN
    "The game you are playing"
    CHARACTER: characters.Character = characters.RAIDEN_SHOGUN
    "The character you are playing"
    HOYOLAB_UID: int = 71845688  # any account that has their game summary on their profile
    "The HoYoLAB UID of the player"
    SERVER_REGION: typing.Optional[regions.Region] = None  # leave as None to take the first one
    "The server region of the player"


@dataclasses.dataclass
class Text:
    """
    Texts for the RPC Client
    
    Availabel variables for the texts:
    - {name}: The nickname of the player
    - {region}: The name of the region the player is playing on
    - {level}: The level (Adventure Rank) of the player
    - {character}: The character the player is playing
    - {game}: The game the player is playing
    """

    STATE_TEXT: str = "{name} 〜 Playing on {region}"
    "The state text that will be displayed. Available variables: {name}, {region}"
    DETAILS_TEXT: str = "Currently at AR {level}"
    "The details text that will be displayed. Available variables: {level}"
    HOVER_TEXT: str = "Come play with me!"
    "The text that will be displayed when the game image is hovered"
    HOVER_CHARACTER_TEXT: str = "My favorite character is {character}"
    "The text that will be displayed when the character image is hovered. Available variables: {character}"


@dataclasses.dataclass
class Settings:
    """Settings for the RPC Client"""

    REFRESH_RATE: typing.Union[int, float] = 60  # in seconds
    "The rate at which the RPC Client will update the presence"
    DISCORD_APPLICATION_ID: int = 929496938020208690  # Put your Discord Application ID if you want to change something
    "The Discord Application ID"
    COOKIE: str = ""
    "The cookie header sent by the browser (you can get it from the network tab in the developer tools of your browser)"

