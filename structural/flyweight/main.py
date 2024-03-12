from factories.abstract_factory import AbstractFactory
from factories.cavalry_factory import CavalryFactory
from factories.infanty_factory import InfantyFactory


def client_code(infanty_fabric: AbstractFactory, cavalry_fabric: AbstractFactory) -> None:
    cavalryes = [cavalry_fabric.create(num) for num in range(5)]
    infantry = [infanty_fabric.create(num) for num in range(5)]

    print("=+="*20)
    for cav in cavalryes:
        print(f"Cavalry {cav.get_number()} media {id(cav.get_media_obj())} coordinates: {cav.get_coordinates_obj().get_coordinates()}")

    print("---"*20)
    for inf in infantry:
        print(f"Infantry {inf.get_number()} media {id(inf.get_media_obj())} coordinates: {inf.get_coordinates_obj().get_coordinates()}")
    print("=+="*20)

calvary_factory = CavalryFactory()
infanty_factory = InfantyFactory()

client_code(infanty_factory, calvary_factory)