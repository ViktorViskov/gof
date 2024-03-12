from .abstract_visitor import AbstractVisitor
from dish.abstract_dish import AbstractDish


class SuppeVisitor(AbstractVisitor):
    _dish: AbstractDish

    def __init__(self, pizza: AbstractDish) -> None:
        self._dish = pizza

    def visit_ananas(self) -> None:
        raise Exception("An ananas is not a suppe ingredient")

    def visit_bacon(self) -> None:
        self._dish.add_ingradient(AbstractDish.Ingradient.BACON)

    def visit_chease(self) -> None:
        self._dish.add_ingradient(AbstractDish.Ingradient.CHEASE)

    def visit_mashrooms(self) -> None:
        self._dish.add_ingradient(AbstractDish.Ingradient.MASHROOMS)

    def visit_seafood(self) -> None:
        raise Exception("A seafood is not a suppe ingredient")
    
    def visit_tomato(self) -> None:
        self._dish.add_ingradient(AbstractDish.Ingradient.TOMATO)