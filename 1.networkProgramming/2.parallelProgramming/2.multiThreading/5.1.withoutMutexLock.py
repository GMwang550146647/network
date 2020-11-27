from threading import Thread
import time

"""
线程之间也有不安全
    1.+=，-= 数据不安全，因为 + 和 赋值是分开的操作 ，自身重新赋值的都不安全例如 a=a+1
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
n = 0
p = []


def add():
    for i in range(300000):
        global n
        global p
        n += 1
        p.append(1)


def sub():
    for i in range(300000):
        global n
        global p
        n -= 1
        if not p:
            time.sleep(0.00000000001)  # 强制线程轮转
        p.pop()  # 这里因为有可能两个线程同时pop，但是len(p)==1，这个时候报错，当只有一个线程的时候就不会


if __name__ == '__main__':
    t_list = []
    n_threads = 5
    add_threads = []
    sub_threads = []
    for i in range(n_threads):
        t1 = Thread(target=add)
        t2 = Thread(target=sub)
        add_threads.append(t1)
        sub_threads.append(t2)
        t1.start()
        t2.start()
    [ti.join() for ti in add_threads]
    [ti.join() for ti in sub_threads]
    print(n)
    print(p)
