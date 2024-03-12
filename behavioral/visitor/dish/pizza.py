from __future__ import annotations

from .abstract_dish import AbstractDish


class Pizza(AbstractDish):
    def __str__(self) -> str:
        result = "Pizza:\n"

        for ingradient, amount in self.ingradients.items():
            result += f" - {ingradient.name}: {amount}\n"
        
        return result
        