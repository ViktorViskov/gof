from datetime import datetime

from abstract_writer import AbstractWriter


class DateWriter(AbstractWriter):
    
    def abstract_write(self) -> None:
        self.file.write(str(datetime.now()))