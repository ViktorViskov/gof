from abstract_sorting import AbstractSorting


class Sorting(AbstractSorting):
    class BubbleStrategy(AbstractSorting):
        def sort(self, array: list[int]) -> list[int]:
            n = len(array)

            for i in range(n):
                for j in range(0, n - i - 1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
    
    class FastSortStrategy(AbstractSorting):
        def sort(self, array: list[int]) -> list[int]:
            if len(array) <= 1:
                return array

            pivot = array[0]
            left = [x for x in array[1:] if x <= pivot]
            right = [x for x in array[1:] if x > pivot]

            return self.sort(left) + [pivot] + self.sort(right)
        
    def sort(self, array: list[int], strategy: AbstractSorting) -> list[int]:
        return strategy.sort(array)