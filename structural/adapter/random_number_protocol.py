from typing import Protocol


class RandomNumberOperations(Protocol):
    def get_random_number(self) -> int:
        pass
    
    def update_random_number(self) -> None:
        pass