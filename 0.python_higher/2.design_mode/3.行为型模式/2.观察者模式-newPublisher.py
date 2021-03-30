from abc import ABCMeta, abstractmethod

'''
1.新闻发布者（被观察的对象）
'''


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detch(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News: {}".format(self.__latestNews)


'''
2.订阅对象（观察对象）
'''


class Subscriber(metaclass=ABCMeta):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):

    def update(self):
        print(f"{type(self).__name__} : {self.publisher.getNews()}")


class EmailSubscriber(Subscriber):

    def update(self):
        print(f"{type(self).__name__} : {self.publisher.getNews()}")


class AnyOtherSubscriber(Subscriber):

    def update(self):
        print(f"{type(self).__name__} : {self.publisher.getNews()}")


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscriber(news_publisher)
    print("Subscribers:", news_publisher.subscribers())
    news_publisher.addNews('Hello Gmwang!')
    news_publisher.notifySubscribers()

    print("Detached:", type(news_publisher.detch()).__name__)
    print("Subscribers:", news_publisher.subscribers())

    news_publisher.addNews("My second news!")
    news_publisher.notifySubscribers()
