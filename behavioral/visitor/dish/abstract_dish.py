from abc import ABC
from enum import Enum


class AbstractDish(ABC):
    class Ingradient(Enum):
        CHEASE = 0
        BACON = 1
        ANANAS = 2
        MASHROOMS = 3
        SEAFOOD = 4
        TOMATO = 5

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

    def add_ingradient(self, ingredient: Ingradient) -> None:
        self.ingradients[ingredient] += 1

    def remove_ingradient(self, ingredient: Ingradient) -> None:
        self.ingradients[ingredient] -= 1