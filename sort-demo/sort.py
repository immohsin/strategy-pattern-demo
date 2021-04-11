import enum


class Sorts(enum.Enum):
    merge_sort =0
    quick_sort = 1
    insertion_sort = 2

class SortImpl:
    def __init__(self, sort):
        self._sort = sort

    def sort_impl(self):
        if self._sort == Sorts.merge_sort:
            self.merge_sort()
        elif self._sort == Sorts.insertion_sort:
            self.insertion_sort()
        elif self._sort == Sorts.quick_sort:
            self.quick_sort()

    def merge_sort(self):
        print("starting merge sort")

    def quick_sort(self):
        print("starting quick sort")

    def insertion_sort(self):
        print("starting insertion sort")
