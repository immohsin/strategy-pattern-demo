from abstract_classes.abstarct_sort import AbstractSortStrategy

class InsertionSortStategy(metaclass=AbstractSortStrategy):
    def sort(self):
        print("starting insertion sort")
