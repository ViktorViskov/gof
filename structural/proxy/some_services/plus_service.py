from .abstract_service import AbstractService


class PlusService(AbstractService):

    def __init__(self) -> None:
        super().__init__()

    def operation(self, num1: int, num2: int) -> int:
        return self.client.service.Add(num1, num2)