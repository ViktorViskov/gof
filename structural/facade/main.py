from facade import Facade


def client_code(facade: Facade):
    print("10 + 2 =", facade.plus(10, 2))
    print("10 - 2 =", facade.minus(10, 2))
    print("10 * 2 =", facade.multiply(10, 2))
    print("10 / 2 =", facade.divide(10, 2))

facade = Facade()
client_code(facade)
