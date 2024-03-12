from .abstract_dish import AbstractDish


class SecondDish(AbstractDish):
    kitchen_name: str
    
    def __init__(self, kitchen_name: str) -> None:
        super().__init__()
        self.kitchen_name = kitchen_name
        
    def get_name(self) -> str:
        return f"{self.kitchen_name} Second Dish"