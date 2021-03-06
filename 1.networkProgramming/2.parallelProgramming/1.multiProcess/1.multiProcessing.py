from multiprocessing import Process
import os
import time
import random

"""
1.进程间可以在一开始传入数据，但是不能返回数据
"""


def func(ith, t=1):
    time.sleep(t)
    print("Process {} received:{}\tpid:{}\tppid:{}".format(ith, t, os.getpid(), os.getppid()))


def create_process(n=4):
    process_list = []
    # 1.设置每个进程任务
    for i in range(n):
        p = Process(target=func, args=(i + 1, random.random() * 3,))
        # 2.异步非阻塞：启动每个进程
        p.start()
        process_list.append(p)
    for i in range(n):
        process_list[i].join()
    print("All Done")


if __name__ == '__main__':
    create_process(4)
