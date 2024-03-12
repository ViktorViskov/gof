from models.pizza import Pizza
from commands.abstract_command import AbstractCommand
from invoker import Invoker
from interpreter import Interpreter


def client_code(invoker: Invoker, root_command: AbstractCommand, pizza: Pizza) -> None:
    invoker.add_command(root_command, pizza)

interpretter = Interpreter("chease ananas chease ananas bacon seafood tomato")
invoker = Invoker()
pizza = Pizza()
root_command = interpretter.get_commands()
client_code(invoker, root_command, pizza)
pizza.show_ingradients()
