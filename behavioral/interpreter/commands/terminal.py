from .abstract_command import AbstractCommand
from models.pizza import Pizza


class TerminalCommand(AbstractCommand):
    _ingradient: Pizza.Ingradient

    def __init__(self, ingradient: Pizza.Ingradient):
        self._ingradient = ingradient

    def invoke(self, pizza: Pizza):
        pizza.add_ingradient(self._ingradient)
    
    def undo(self, pizza: Pizza):
        pizza.remove_ingradient(self._ingradient)