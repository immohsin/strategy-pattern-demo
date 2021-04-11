from abstract_classes.abstarct_sort import AbstractSortStrategy


class DoSort:
    def __init__(self, strategy: AbstractSortStrategy):
        self._strategy = strategy
    
    def do_sort(self):
        self._strategy.sort()
