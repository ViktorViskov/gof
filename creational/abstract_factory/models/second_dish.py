from .idish import IDish


class SecondDish(IDish):
    def get_name(self, kitchen: str) -> None:
        print(f"{kitchen} Second Dish")