'''
保护本体的代理，不直接访问本体，而是通过代理只访问本体的一部分功能！
'''

'''
1.本体
'''


class Actor():
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, 'is occupied with current movie')

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy


'''
2.代理： 只可以获取本体的某些功能！
'''


class Agent():
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
