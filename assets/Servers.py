class Server():
    def __init__(self, name: str, code: str) -> None:
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        return "Server({})".format(self.name)


EUROPE = Server("Europe", "os_euro")
