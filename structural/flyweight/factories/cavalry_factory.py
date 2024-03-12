from models.cavalry import Cavalry
from .abstract_factory import AbstractFactory


class CavalryFactory(AbstractFactory):

    def create(self, num: int) -> Cavalry:
        return Cavalry(self._create_coordinates(), self._get_media("cavalry"), num)