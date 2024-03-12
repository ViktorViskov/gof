from decorator.pizza_decorator import PizzaDecorator 
from decorator.ananas_decorator import AnanasDecorator
from decorator.bacon_decorator import BaconDecorator
from decorator.chease_decorator import CheaseDecorator
from decorator.mashrooms_decorator import MashroomsDecorator
from decorator.seafood_decorator import SeafoodDecorator
from decorator.tomato_decorator import TomatoDecorator
from models.pizza import Pizza


def client_code(decorator: PizzaDecorator) -> None:
    pizza = decorator.create()
    pizza.show_ingradients()

decorator_one = AnanasDecorator(BaconDecorator(CheaseDecorator(CheaseDecorator(MashroomsDecorator(SeafoodDecorator(TomatoDecorator(Pizza())))))))
decorator_two = AnanasDecorator(BaconDecorator(CheaseDecorator(SeafoodDecorator(TomatoDecorator(Pizza()))))).create()
decorator_three = BaconDecorator(AnanasDecorator(Pizza())).create()

client_code(decorator_one)
client_code(decorator_two)
client_code(decorator_three)


