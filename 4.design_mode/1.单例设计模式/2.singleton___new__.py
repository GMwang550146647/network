from fundamentals.test_time import test_time
from threading import Thread


class Singleton():
    _instance = None

    def __init__(self, x):
        self.x = x

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print(f"Initial cls ->              {cls._instance}")
        else:
            print(f"Cls already initialized ->  {cls._instance}")
        return cls._instance

    def this_is_a_private_function(self):
        print(f'{self.x}: {self} activated this private function (only allow one obj use!)')


def test_thread_safe(n=1):
    ts = []
    for i in range(n):
        ti = Thread(target=Singleton, args=(i,))
        ts.append(ti)
    [ti.start() for ti in ts]
    [ti.join() for ti in ts]


def test_singleton():
    '''
    1.测试单例模式是否正常运行
    '''
    a1 = Singleton(1)
    a2 = Singleton(2)
    print(a1.x)
    print(a2.x)

    '''
    2.有个小小的漏洞，能通过修改a1.__class__._instance 从而让下一个 实例能被创建
    '''
    k1 = a1.__class__._instance
    a1.__class__._instance = None
    k2 = Singleton(3)
    a1.this_is_a_private_function()
    k2.this_is_a_private_function()
    # 而且两个的实例不一样！
    print(k1)
    print(k2._instance)


if __name__ == '__main__':
    # test_singleton()
    # test_thread_safe()
    k=Singleton(10)
    k1=k._instance
    k1.__init__(1000)
    print(k.x)