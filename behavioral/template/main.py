from abstract_writer import AbstractWriter
from text_writer import TextWriter
from date_writer import DateWriter


def client_code(writer: AbstractWriter) -> None:
    writer.write()

client_code(TextWriter("text.txt"))
client_code(DateWriter("date.txt"))