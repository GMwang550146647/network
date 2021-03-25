from fundamentals.test_time import test_time
from threading import Thread, Lock


class Singleton():
    _instance = None
    _instance_lock = Lock()

    def __init__(self, x):
        self.x = x

    def __new__(cls, *args, **kwargs):
        # 看看cls._instance 有没有被占用
        if cls._instance is None:
            with cls._instance_lock:
                # 看看获取锁的期间 cls._instance 有没有被抢
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print(f"Initial cls ->              {cls._instance}")
                    return cls._instance
        else:
            print(f"Cls already initialized ->  {cls._instance}")
            return cls._instance



def thread_safe(n=40):
    ts = []
    for i in range(n):
        ti = Thread(target=Singleton, args=(i,))
        ts.append(ti)
    [ti.start() for ti in ts]
    [ti.join() for ti in ts]


if __name__ == '__main__':
    thread_safe()
