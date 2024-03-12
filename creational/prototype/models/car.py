from __future__ import annotations

from models.car_type import CarType


class Car:
    car_type: CarType
    color: str
    number: int
    manufacturer: str

    def __init__(self, car_type: CarType, color: str, number: int, manufacturer: str):
        self.car_type = car_type
        self.color = color
        self.number = number
        self.manufacturer = manufacturer
    
    def get_name(self) -> str:
        return f"{self.manufacturer} {self.car_type.name} {self.color} {self.number}"
    
    def copy(self, color: str, number: int) -> Car:
        return self.__class__(self.car_type, color, number, self.manufacturer)