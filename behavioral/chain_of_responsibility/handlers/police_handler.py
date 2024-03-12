from .abstract_handler import AbstractHandler


class PoliceHandler(AbstractHandler):
    def can_do(self, target: str) -> bool:
        return "police" in target.lower()
    
    def do(self) -> str:
        return "Police department"