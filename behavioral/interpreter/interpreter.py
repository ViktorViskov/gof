from commands.abstract_command import AbstractCommand
from commands.non_terminal import NonTerminalCommand
from commands.terminal import TerminalCommand
from models.pizza import Pizza


class Interpreter:
    expressions: list[str]
    _bindings = {
        "chease": Pizza.Ingradient.CHEASE,
        "bacon": Pizza.Ingradient.BACON,
        "mashrooms": Pizza.Ingradient.MASHROOMS,
        "seafood": Pizza.Ingradient.SEAFOOD,
        "tomato": Pizza.Ingradient.TOMATO,
        "ananas": Pizza.Ingradient.ANANAS
    }

    def __init__(self, expression: str) -> None:
        self.expressions = expression.lower().split(" ")

    def get_commands(self) -> AbstractCommand:
        root_command: AbstractCommand = None
        last_command: NonTerminalCommand = None
        
        while self.expressions:
            expression = self.expressions.pop()

            if self.expressions:
                command = NonTerminalCommand(self._bindings[expression])

                if last_command:
                    last_command.set_command(command)
                else:
                    root_command = command

                last_command = command

            else:
                command = TerminalCommand(self._bindings[expression])
                
                if last_command:
                    last_command.set_command(command)
                else:
                    root_command = command

        return root_command
            