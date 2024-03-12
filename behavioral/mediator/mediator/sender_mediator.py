from .abstract_mediator import AbstractMediator
from sender import Sender


class SenderMediator(AbstractMediator):
    def send_message(self, message: str) -> bool:
        return Sender.send_message(message)