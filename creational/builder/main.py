from builder.hawaii_pizza_builder import HawaiiPizzaBuilder
from builder.seafood_pizza_builder import SeafoodPizzaBuilder
from builder.custom_pizza_builder import CustomPizzaBuilder


pizza_builder = SeafoodPizzaBuilder()
pizza_builder.add_mashrooms()
pizza_builder.add_chease()
pizza_builder.add_tomato()
pizza = pizza_builder.make()
pizza.show_ingradients()

pizza_builder = HawaiiPizzaBuilder()
pizza_builder.add_ananas()
pizza_builder.add_chease()
pizza_builder.add_tomato()
pizza = pizza_builder.make()
pizza.show_ingradients()

pizza_builder = CustomPizzaBuilder()
pizza_builder.add_ananas()
pizza_builder.add_chease()
pizza_builder.add_tomato()
pizza = pizza_builder.make()
pizza.show_ingradients()
