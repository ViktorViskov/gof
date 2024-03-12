from __future__ import annotations

from .abstract_dish import AbstractDish


class Suppe(AbstractDish):
    def __str__(self) -> str:
        result = "Suppe:\n"

        for ingradient, amount in self.ingradients.items():
            result += f" - {ingradient.name}: {amount}\n"
        
        return result
        