from multiprocessing import Process
from threading import Thread
import os
import time
import random



def func(ith, t=1):
    print("Process {} received:{}\tpid:{}\tppid:{}".format(ith, t, os.getpid(), os.getppid()))


def create_process(n=4,execuate=Thread):
    process_list = []
    # 1.设置每个进程任务
    for i in range(n):
        p = execuate(target=func, args=(i + 1, random.random() * 3,))
        # 2.异步非阻塞：启动每个进程
        p.start()
        process_list.append(p)
    print("Finished Creating All Process/Thread")
    for i in range(n):
        process_list[i].join()
    print("All Tasks Done")


if __name__ == '__main__':
    create_process(execuate=Thread)
    print("________________THIS IS A SEPARATION LINE________________")
    create_process(execuate=Process)
