from commands.abstract_command import AbstractCommand


class Invoker:
    do: list[AbstractCommand]
    undo: list[AbstractCommand]
    doing: list[AbstractCommand]

    def __init__(self):
        self.do = []
        self.undo = []
        self.doing = []

    def _execute_commands(self) -> None:
        while len(self.doing):
            command = self.doing.pop()
            command.invoke()
            self.undo.append(command)

    def add_command(self, command: AbstractCommand) -> None:
        self.doing.append(command)
        self._execute_commands()
    
    def undo_last_command(self) -> None:
        if len(self.undo):
            command = self.undo.pop()
            command.undo()
            self.do.append(command)

    def redo_last_command(self) -> None:
        if len(self.do):
            command = self.do.pop()
            command.invoke()
            self.undo.append(command)