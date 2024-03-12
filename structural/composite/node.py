from element import Element


class Node(Element):
    elements: list[Element]
    
    def __init__(self, *elements: list[Element]) -> None:
        super().__init__()
        self.elements = elements
    
    def increment(self):
        self.number += 1
        print(f"Node id: {id(self)} incremented to {self.number}")
        
        for element in self.elements:
            element.increment()
        
    def decrement(self):
        self.number -= 1
        print(f"Node id: {id(self)} decremented to {self.number}")
        
        for element in self.elements:
            element.decrement()
