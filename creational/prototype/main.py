from functools import partial

from models.car import Car
from models.car_type import CarType


car = Car(CarType.SEDAN, "red", 123456, "Volvo")
print(car.get_name())

car1 = car.copy("blue", 234567)
print(car1.get_name())

car2 = partial(car.copy, color="white", number=122213)()
print(car2.get_name())
