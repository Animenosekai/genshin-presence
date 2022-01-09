from assets import Characters, Games, Servers


class Player:
    GAME = Games.GENSHIN
    CHARACTER = Characters.RAIDEN_SHOGUN
    HOYOLAB_UID = 71845688  # any account that has their game summary on their profile
    SERVER_REGION = None  # leave as None to take the first one


class Text:
    TEXT = "Come play with me!"  # when the game image is hovered
    CHARACTER_TEXT = None  # keep it None to define this automatically, it defines the text when the character is hovered


class Settings:
    REFRESH_RATE = 60  # in seconds
    # just copy and paste the cookie header sent by the browser
    COOKIE = ""
