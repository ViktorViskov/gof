from element import Element


class Leaf(Element):
    def increment(self):
        self.number += 1
        print(f"Leaf id: {id(self)} incremented to {self.number}")
        
    def decrement(self):
        self.number -= 1
        print(f"Leaf id: {id(self)} decremented to {self.number}")
