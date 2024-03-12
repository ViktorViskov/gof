from .abstract_service import AbstractService


class PlusService(AbstractService):
    def operation(self, num1: int, num2: int) -> int:
        return self.client.service.Add(num1, num2)