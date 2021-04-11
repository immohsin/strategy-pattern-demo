from abstract_classes.abstarct_sort import AbstractSortStrategy

class QuickSortStategy(metaclass=AbstractSortStrategy):
    def sort(self):
        print("starting quick sort")
