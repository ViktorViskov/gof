from __future__ import annotations
from abc import ABC
from abc import abstractmethod


class AbstractPizza(ABC):
    chease = 0
    bacon = 0
    ananas = 0
    mashrooms = 0
    seafood = 0
    tomato = 0
    
    @abstractmethod    
    def create(self) -> AbstractPizza:
        pass
    
    def add_chease(self) -> None:
        self.chease += 1
        
    def add_bacon(self) -> None:
        self.bacon += 1
        
    def add_ananas(self) -> None:
        self.ananas += 1
        
    def add_mashrooms(self) -> None:
        self.mashrooms += 1
    
    def add_seafood(self) -> None:
        self.seafood += 1
        
    def add_tomato(self) -> None:
        self.tomato += 1
    
    def show_ingradients(self) -> None:
        print("-" * 20)
        print("Pizza Ingredients:")
        print("-" * 20)
        print(f"{self.__class__.__name__} Ingredients:")
        print(f"Chease: {self.chease}")
        print(f"Bacon: {self.bacon}")
        print(f"Ananas: {self.ananas}")
        print(f"Tomato: {self.tomato}")
        print(f"Mashrooms: {self.mashrooms}")
        print(f"Seafood: {self.seafood}")
        print("*" * 20)
