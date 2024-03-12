from models.infantry import Infanty
from .abstract_factory import AbstractFactory


class InfantyFactory(AbstractFactory):

    def create(self, num: int) -> Infanty:
        return Infanty(self._create_coordinates(), self._get_media("cavalry"), num)