"""
线程基本使用
    1.线程开启比进程快很多
    2.线程无法terminate，只能自己结束

基本
    # 1.current_thread()  返回当前线程的对象， ident->其id
    # 2.enumerate() 返回所有活着的线程
    # 3.active_count 返回活着的线程数量
"""
from threading import Thread, current_thread, enumerate, active_count
# from multiprocessing import Process as Thread
import time
import os


def func(i):
    # 1.current_thread()  返回当前线程的对象， ident->其id
    print("current thread:{}  ->start{}".format(current_thread().ident, i))
    time.sleep(1)
    print("current thread:{}  ->end{}".format(current_thread(), i))


if __name__ == '__main__':
    t_list = []
    for i in range(10):
        ti = Thread(target=func, args=(i + 1,))
        ti.start()
        print("Thread {} -> tid:{} pid:{} ppid:{}".format(i, ti.ident, os.getpid(), os.getppid()))
        t_list.append(ti)
    # 2.enumerate() 返回所有活着的线程
    print(enumerate())
    # 3.active_count 返回活着的线程数量
    print(active_count())
    # 异步阻塞（如果不join就是异步非阻塞）
    [ti.join() for ti in t_list]
    print("All Done")
