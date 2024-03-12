from factories import AbstractFactory
from factories import PizzaFactory
from factories import BreadFactory


def client_code(creator: AbstractFactory) -> None:
    dish = creator.create_dish()
    print(dish.get_name())

creator_bread = BreadFactory()
client_code(creator_bread)

creator_cake = PizzaFactory()
client_code(creator_cake)
