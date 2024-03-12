from .abstract_command import AbstractCommand
from models.pizza import Pizza


class TomatoCommand(AbstractCommand):
    pizza: Pizza

    def __init__(self, pizza):
        self.pizza = pizza

    def invoke(self):
        self.pizza.add_ingradient(Pizza.Ingradient.TOMATO)

    def undo(self):
        self.pizza.remove_ingradient(Pizza.Ingradient.TOMATO)
