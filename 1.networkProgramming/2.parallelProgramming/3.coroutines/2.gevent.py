
"""
monkey.patch_all()能让各种io函数变成协程版本
例如
    time.sleep()  ->  gevent.sleep() 成为可并发模式
"""
from gevent import monkey
monkey.patch_all()
import gevent
import time


def run_func(n_gevent=10):
    def func(i):
        print("start func {}".format(i))
        # 这个原本不是gevent内置的规避io的操作 ->变成协程版本的函数了
        time.sleep(1)
        print('end func {}'.format(i))
    g_list = []
    for i in range(n_gevent):
        gi = gevent.spawn(func, i=i)
        g_list.append(gi)
    # for gi in g_list: gi.join()
    gevent.joinall(g_list)

if __name__ == '__main__':
    run_func()