from server import Server


class Adapter:
    def __init__(self, server: Server) -> None:
        self.server = server

    def get_random_number(self) -> int:
        return self.server.otrumati_chislo()

    def update_random_number(self) -> None:
        self.server.obnovi_chislo()