from abc import ABC
from abc import abstractmethod
from random import randint

from models.media import Media
from models.coordinates import Coordinates
from models.unit import Unit


class AbstractFactory(ABC):
    media: dict[str, Media]
    coordinates: list[Coordinates]

    def __init__(self) -> None:
        self.media = {}
        self.coordinates = []

    def _get_media(self, key: str) -> Media:
        media = self.media.get(key)
        if not media:
            media = Media()
            self.media[key] = media
        return media
    
    def _create_coordinates(self) -> Coordinates:
        coordinates = Coordinates(randint(0, 100), randint(0, 100), randint(0, 100))
        self.coordinates.append(coordinates)
        return coordinates
    
    @abstractmethod
    def create(self, num: int) -> Unit:
        pass