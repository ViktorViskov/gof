from node import Node
from leaf import Leaf


root = Node(
    Leaf(),
    Node(
        Node(
            Leaf(),
            Leaf(),
        ),
        Leaf(),
    ),
)
    
print("--"*30)
root.increment()
print("--"*30)
root.increment()
print("--"*30)
root.decrement()