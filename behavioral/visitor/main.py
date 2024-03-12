from ingradients.abstract_ingradient import AbstractIngradient
from ingradients.bacon_ingradient import BaconIngradient
from ingradients.mashrooms_ingradient import MashroomsIngradient
from ingradients.seafood_ingradient import SeafoodIngradient
from ingradients.tomato_ingradient import TomatoIngradient


from visitor.abstract_visitor import AbstractVisitor
from visitor.pizza_visitor import PizzaVisitor
from visitor.suppe_visitor import SuppeVisitor
from dish.pizza import Pizza
from dish.suppe import Suppe


def client_code(ingradients: list[AbstractIngradient], visitor: AbstractVisitor) -> None:
    for ingradient in ingradients:
        ingradient.accept(visitor)

ingradients = (
    BaconIngradient(),
    MashroomsIngradient(),
    MashroomsIngradient(),
    SeafoodIngradient(),
    TomatoIngradient(),
)

pizza = Pizza()
pizza_visitor = PizzaVisitor(pizza)
client_code(ingradients, pizza_visitor)
print(pizza)

suppe = Suppe()
suppe_visitor = SuppeVisitor(suppe)
client_code(ingradients, suppe_visitor)
print(suppe)
