from threading import Thread,Lock
import time
"""
线程之间也有不安全
    1.+=，-= 数据不安全，因为 + 和 赋值是分开的操作
          5           0 LOAD_GLOBAL              0 (a)
                      2 LOAD_CONST               1 (1)
        ->非原子操作    4 INPLACE_ADD
        ->非原子操作   6 STORE_GLOBAL             0 (a)
                      8 LOAD_CONST               0 (None)
                     10 RETURN_VALUE
    2. append pop 安全 但是if，while操作不安全（所以还是要加锁）
          9           0 LOAD_GLOBAL              0 (p)
                      2 LOAD_METHOD              1 (append)
                      4 LOAD_CONST               1 (1)
        ->原子操作     6 CALL_METHOD              1
                     8 POP_TOP
                     10 LOAD_CONST               0 (None)
                     12 RETURN_VALUE
"""
n=0
def add(lock):
    for i in range(300000):
        with lock:
            global n
            n += 1
def sub(lock):
    for i in range(300000):
        with lock:
            global n
            n -= 1

if __name__ == '__main__':
    lock=Lock()
    t_list = []
    n_threads = 5
    add_threads = []
    sub_threads = []
    for i in range(n_threads):
        t1 = Thread(target=add,args=(lock,))
        t2 = Thread(target=sub,args=(lock,))
        add_threads.append(t1)
        sub_threads.append(t2)
        t1.start()
        t2.start()
    [ti.join() for ti in add_threads]
    [ti.join() for ti in sub_threads]
    print(n)
