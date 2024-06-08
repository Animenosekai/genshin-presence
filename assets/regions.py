import dataclasses


@dataclasses.dataclass(frozen=True)
class Region:
    name: str
    code: str


EUROPE = Region(name="Europe", code="os_euro")

