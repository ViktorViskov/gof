from .coordinates import Coordinates
from .media import Media


class Unit:
    coordinates: Coordinates
    media: Media
    number: int

    def __init__(self, coordinates: Coordinates, media: Media, number: int) -> None:
        self.coordinates = coordinates
        self.media = media
        self.number = number
    
    def get_coordinates_obj(self) -> Coordinates:
        return self.coordinates
    
    def get_media_obj(self) -> Media:
        return self.media
    
    def get_number(self) -> int:
        return self.number