from .idish import IDish


class Pizza(IDish):
    def get_name(self) -> None:
        return "I am a pizza"