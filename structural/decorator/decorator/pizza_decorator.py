from models.abstract_pizza import AbstractPizza


class PizzaDecorator(AbstractPizza):
    _subject: AbstractPizza
    
    def __init__(self, pizza: AbstractPizza) -> None:
        self._subject = pizza
        
    @property
    def subject(self) -> AbstractPizza:
        return self._subject
        
    def add_chease(self) -> None:
        self._subject.add_chease()
        
    def add_bacon(self) -> None:
        self._subject.add_bacon()
        
    def add_ananas(self) -> None:
        self._subject.add_ananas()
        
    def add_mashrooms(self) -> None:
        self._subject.add_mashrooms()
    
    def add_seafood(self) -> None:
        self._subject.add_seafood()
        
    def add_tomato(self) -> None:
        self._subject.add_tomato()
            
    def create(self) -> AbstractPizza:
        return self._subject.create()