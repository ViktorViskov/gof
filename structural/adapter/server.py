from random import randint


class Server:
    chislo: int
    
    def __init__(self) -> None:
        self.chislo = randint(1, 10000)
        
    def otrumati_chislo(self) -> int:
        return self.chislo
    
    def obnovi_chislo(self) -> None:
        self.chislo = randint(1, 10000)
    