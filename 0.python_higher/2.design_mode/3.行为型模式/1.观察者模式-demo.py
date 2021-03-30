class Subject:
    def __init__(self):
        self.__observer = []

    def register(self, observer):
        self.__observer.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observer:
            observer.notify(self, *args, **kwargs)


from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    def __init__(self, subject):
        subject.register(self)

    @abstractmethod
    def notify(self, subject, *args, **kwargs):
        pass


class Observer1(Observer):
    def notify(self, subject, *args, **kwargs):
        print(f"{type(self).__name__} Got {args} From {subject}")


class Observer2(Observer):
    def notify(self, subject, *args, **kwargs):
        print(f"{type(self).__name__} Got {args} From {subject}")


if __name__ == '__main__':
    sj = Subject()
    o1 = Observer1(sj)
    o2 = Observer2(sj)
    sj.notifyAll('hello world')
