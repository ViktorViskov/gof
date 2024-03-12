from ordinator import Ordinator
from memento import Memento


class Editor(Ordinator):
    _content: str = ""

    def set_content(self, content: str) -> None:
        self._content = content

    def get_content(self) -> str:
        return self._content
    
    def get_state(self) -> Memento:
        return Memento(self._content)

    def restore_state(self, state: Memento) -> None:
        self._content = state.get_state()
