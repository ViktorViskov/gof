from .abstract_pizza import AbstractPizza


class Pizza(AbstractPizza):
    def create(self) -> AbstractPizza:
        return self
