from .idish import IDish


class FirstDish(IDish):
    def get_name(self, kitchen: str) -> None:
        print(f"{kitchen} First Dish")