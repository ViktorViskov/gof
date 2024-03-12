from abc import ABC
from abc import abstractmethod
from io import TextIOWrapper


class AbstractWriter(ABC):
    _file_name: str
    file: TextIOWrapper

    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    def _open_file(self) -> None:
        self.file = open(self._file_name, "w")

    def _close_file(self) -> None:
        self.file.close()

    def write(self) -> None:
        self._open_file()
        self.abstract_write()
        self._close_file()

    @abstractmethod
    def abstract_write(self) -> None:
        pass