from .abstract_handler import AbstractHandler


class ErrorHandler(AbstractHandler):
    def can_do(self, _: str) -> bool:
        return True
    
    def do(self) -> str:
        return "Error handler"