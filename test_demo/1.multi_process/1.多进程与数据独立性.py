from multiprocessing import Process
import os
import time
import random

"""
1.进程间可以在一开始传入数据，但是不能返回数据
"""
base_t=0.4
def func(ith, t=1):
    global base_t
    base_t+=0.1
    time.sleep(t+base_t)
    print("Process {} received:t: {} base_t: {}\tpid:{}\tppid:{}".format(ith, t,base_t, os.getpid(), os.getppid()))
    return t
def create_process(n=4):
    process_list = []
    # 1.设置每个进程任务
    for i in range(n):
        p = Process(target=func, args=(i + 1, random.random() * 2,))
        # 2.异步非阻塞：启动每个进程
        p.start()
        process_list.append(p)
        time.sleep(0.00001)
    for i in range(n):
        process_list[i].join()
    print("All Done")
if __name__ == '__main__':
    create_process(4)
