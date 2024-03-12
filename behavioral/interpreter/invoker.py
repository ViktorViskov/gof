from commands.abstract_command import AbstractCommand
from models.pizza import Pizza


class Invoker:
    do: list[AbstractCommand]
    undo: list[AbstractCommand]
    doing: list[AbstractCommand]

    def __init__(self):
        self.do = []
        self.undo = []
        self.doing = []

    def _execute_commands(self, pizza: Pizza) -> None:
        while len(self.doing):
            command = self.doing.pop()
            command.invoke(pizza)
            self.undo.append(command)

    def add_command(self, command: AbstractCommand, pizza: Pizza) -> None:
        self.doing.append(command)
        self._execute_commands(pizza)
    
    def undo_last_command(self, pizza: Pizza) -> None:
        if len(self.undo):
            command = self.undo.pop()
            command.undo(pizza)
            self.do.append(command)

    def redo_last_command(self, pizza: Pizza) -> None:
        if len(self.do):
            command = self.do.pop()
            command.invoke(pizza)
            self.undo.append(command)