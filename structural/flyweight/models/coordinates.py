class Coordinates:
    x: int
    y: int
    z: int

    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self) -> tuple[int, int, int]:
        return self.x, self.y, self.z
    
    def set_coordinates(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z