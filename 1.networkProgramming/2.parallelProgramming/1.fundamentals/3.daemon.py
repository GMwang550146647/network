import time
from multiprocessing import Process

"""
守护进程（daemon)
    特点：
        1.守护进程等待主进程代码结束而结束
        2.主进程最后会回收守护进程的PCB等资源
"""


def fun1():
    t = 0
    while True:
        t += 1
        time.sleep(1)
        print("In fun1, waited for {} s".format(t))


def fun2():
    for i in range(10):
        time.sleep(1)
        print("In fun2, waited for {} s".format(i + 1))


if __name__ == '__main__':
    #1.p1守护进程
    p1 = Process(target=fun1)
    # 设置守护进程（daemon)
    p1.daemon = True
    p1.start()
    #2.p2普通进程
    p2 = Process(target=fun2).start()
    time.sleep(3)
    #3.主程序代码结束，daemon进程随之结束，但是主程序并没完全结束，他等待p2结束，然后回收p1，p2进程资源
    print("Main Exit!")
