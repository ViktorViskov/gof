from models.pizza import Pizza
from commands.abstract_command import AbstractCommand
from commands.chease_command import CheaseCommand
from commands.bacon_command import BaconCommand
from commands.mashrooms_command import MashroomsCommand

from invoker import Invoker


def client_code(invoker: Invoker, commands: list[AbstractCommand]) -> None:
    for command in commands:
        invoker.add_command(command)

    # undo last command
    invoker.undo_last_command()

invoker = Invoker()
pizza = Pizza()
commands = [
    CheaseCommand(pizza),
    CheaseCommand(pizza),
    BaconCommand(pizza),
    MashroomsCommand(pizza),
]

client_code(invoker, commands)
pizza.show_ingradients()
