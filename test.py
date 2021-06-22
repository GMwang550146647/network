from abc import ABCMeta,abstractmethod

class Base(ABCMeta):
    @abstractmethod
    def func(cls):
        pass