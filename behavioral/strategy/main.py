from abstract_sorting import AbstractSorting
from sorting import Sorting
from random import shuffle
from datetime import datetime


def client_code(sorting: AbstractSorting) -> None:
    numbers_one = (list(range(10000)))
    shuffle(numbers_one)
    numbers_two = numbers_one.copy()

    start_one = datetime.now()
    items_one = sorting.sort(numbers_one, Sorting.BubbleStrategy())
    end_one = datetime.now()

    start_two = datetime.now()
    items_two = sorting.sort(numbers_two, Sorting.FastSortStrategy())
    end_two = datetime.now()

    print(f"Bubble sort: {end_one - start_one}")
    print(f"Fast sort: {end_two - start_two}")

sorting = Sorting()
client_code(sorting)