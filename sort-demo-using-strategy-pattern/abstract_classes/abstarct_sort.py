from abc import ABCMeta, abstractmethod


class AbstractSortStrategy(ABCMeta):
    @abstractmethod
    def sort():
        raise NotImplementedError()