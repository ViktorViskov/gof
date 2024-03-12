from kitchen.abstract_kitchen import AbstractKitchen


class Restorant:
    def __init__(self, kitchen: AbstractKitchen) -> None:
        self.kitchen = kitchen
        
    def order_first(self) -> str:
        return self.kitchen.create_first().get_name()
    
    def order_second(self) -> str:
        return self.kitchen.create_second().get_name()
    
    def order_third(self) -> str:
        return self.kitchen.create_third().get_name()
    
    def order_desert(self) -> str:
        return self.kitchen.create_desert().get_name()