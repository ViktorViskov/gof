from .abstract_handler import AbstractHandler


class FireHandler(AbstractHandler):
    def can_do(self, target: str) -> bool:
        return "fire" in target.lower()
    
    def do(self) -> str:
        return "Fire department"