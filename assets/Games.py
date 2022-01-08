class Game():
    def __init__(self, name: str, code: int, image: str) -> None:
        self.name = name
        self.code = code
        self.image = image

    def __repr__(self) -> str:
        return "Game({})".format(self.name)


HONKAI = Game("Honkai Impact 3rd", 1, "game-honkai-3rd")
GENSHIN = Game("Genshin Impact", 2, "game-genshin")
