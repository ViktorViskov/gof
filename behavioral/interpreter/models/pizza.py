from __future__ import annotations
from enum import Enum


class Pizza:
    ingradients: dict[Ingradient, int]

    def __init__(self):
        self.ingradients = {
            self.Ingradient.CHEASE: 0,
            self.Ingradient.BACON: 0,
            self.Ingradient.ANANAS: 0,
            self.Ingradient.MASHROOMS: 0,
            self.Ingradient.SEAFOOD: 0,
            self.Ingradient.TOMATO: 0
        }

    class Ingradient(Enum):
        CHEASE = 0
        BACON = 1
        ANANAS = 2
        MASHROOMS = 3
        SEAFOOD = 4
        TOMATO = 5

    def add_ingradient(self, ingredient: Ingradient) -> None:
        self.ingradients[ingredient] += 1

    def remove_ingradient(self, ingredient: str) -> None:
        self.ingradients[ingredient] -= 1

    def show_ingradients(self) -> None:
        print("+" * 30)
        print(f"{self.__class__.__name__} Ingredients:")
        for ingradient, amount in self.ingradients.items():
            print(f"{ingradient.name}: {amount}")
        print("-" * 30)
        