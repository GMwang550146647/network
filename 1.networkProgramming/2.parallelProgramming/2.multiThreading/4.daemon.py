import time
from threading import Thread

"""
主线程等待子线程结束才会结束
主线程结束，进程就会结束
守护线程（daemon)
    特点： 
        随着主线程结束而结束（注意，是主线程结束，而不是主线程代码结束）
        ->对比进程，守护进程只等到主进程代码结束就结束了，不等其他子进程
        如果主线程代码结束还有其他子线程在运行，守护线程也守护
    为什么？
        守护线程和守护进程的结束原理不一样
        守护进程需要主进程来回收资源
        守护线程是随着进程结束才结束的
            其他子线程结束-> 主线程结束 -> 主进程结束 -> 整个进程中所有资源被回收 -> 守护线程也被回收
"""


def fun1():
    t = 0
    while True:
        t += 1
        time.sleep(1)
        print("Daemon fun1, still alive waited for {} s".format(t))


def fun2():
    for i in range(10):
        time.sleep(1)
        print("In fun2, waited for {} s".format(i + 1))


if __name__ == '__main__':
    #1.p1守护线程
    p1 = Thread(target=fun1)
    # 设置守护线程（daemon)
    p1.daemon = True
    p1.start()
    #2.p2普通线程
    p2 = Thread(target=fun2).start()
    time.sleep(3)
    #3.主程序代码结束，daemon进程随之结束，但是主程序并没完全结束，他等待p2结束，然后回收p1，p2进程资源
    print("Main Exit!")
