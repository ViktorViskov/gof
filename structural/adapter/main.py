from random_number_protocol import RandomNumberOperations
from adapter import Adapter
from server import Server


def client_code(adapter: RandomNumberOperations) -> None:
    print(f"Random number: {adapter.get_random_number()}")
    adapter.update_random_number()
    print(f"Random number: {adapter.get_random_number()}")
    
adapter = Adapter(Server())
client_code(adapter)