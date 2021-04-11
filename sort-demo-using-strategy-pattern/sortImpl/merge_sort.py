from abstract_classes.abstarct_sort import AbstractSortStrategy

class MergeSortStategy(metaclass=AbstractSortStrategy):
    def sort(self):
        print("starting merge sort")
