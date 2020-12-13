from threading import Thread,current_thread
import time
import os

n = 10


def func():
    global n
    print("Thread {} \t  received:n: {}\tpid:{}\tppid:{}".format(current_thread(), n,  os.getpid(), os.getppid()))
    n -= 1
    time.sleep(0.1)


def create_thread(n_threads=10):
    t_list = []
    tempt_n=n
    for i in range(n_threads):
        t = Thread(target=func)
        t.start()
        t_list.append(t)
    for t in t_list: t.join()
    print("After {} times : Reduce from {} to {}".format(n_threads,tempt_n,n))


if __name__ == '__main__':
    create_thread()
