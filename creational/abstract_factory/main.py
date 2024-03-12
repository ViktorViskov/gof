from factories.abstract_factory import AbstractFactory
from factories.american_dish_factory import AmericanDishFactory
from factories.japanese_dish_factory import JapaneseDishFactory
from factories.ukraine_dish_factory import UkrainianDishFactory


def client_code(creator: AbstractFactory):
    first = creator.create_first()
    second = creator.create_second()

    first.get_name(creator.__class__.__name__)
    second.get_name(creator.__class__.__name__)

japan_kitchen = JapaneseDishFactory()
client_code(japan_kitchen)

american_kitchen = AmericanDishFactory()
client_code(american_kitchen)

ukraine_kitchen = UkrainianDishFactory()
client_code(ukraine_kitchen)
