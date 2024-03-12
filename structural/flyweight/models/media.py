class Media:
    textures: list[str]
    audios: list[str]

    def __init__(self) -> None:
        self.textures = []
        self.audios = []