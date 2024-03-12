import contextvars

from singleton import Singleton
from multiton import Multiton


global_context = contextvars.ContextVar('global_singleton')

print("Show singleton object ids:")
for num in range(3):
    item = Singleton.get_instance()
    print(f"{num}:", id(item), sep="\t")

# test for multiton
print("Show multiton object ids:")
for num in range(12):
    item = Multiton.get_instance()
    print(f"{num}:", id(item), sep="\t")
