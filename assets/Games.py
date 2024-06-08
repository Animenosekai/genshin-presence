import dataclasses
import pathlib


@dataclasses.dataclass(frozen=True)
class Game:
    name: str
    code: int
    image: str

    @property
    def image_path(self):
        """"""
        return (pathlib.Path(__file__).parent / "games" / self.image).with_suffix(
            ".png"
        )


HONKAI = Game("Honkai Impact 3rd", 1, "game-honkai-3rd")
GENSHIN = Game("Genshin Impact", 2, "game-genshin")

