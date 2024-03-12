from abstract_writer import AbstractWriter


class TextWriter(AbstractWriter):
    
    def abstract_write(self) -> None:
        self.file.write("Writing to file")