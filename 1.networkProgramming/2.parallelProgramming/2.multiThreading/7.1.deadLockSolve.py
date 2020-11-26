# from threading import Thread, Lock
from threading import Thread, RLock

"""
死锁出现的核心原因
    多把锁，多个线程之间，交叉使用
死锁原因
    eat1 与eat2 拿面和叉子的顺序不一样，最后一个人拿着叉子，一个人拿着面，就死锁了

解决方法：
    把所有的锁弄成一把递归锁，但是锁多次就行了
    或者把所有锁合成一把，或者把大家拿放锁的顺序一致
"""


def eat1(name, noodle_lock, fork_lock):
    noodle_lock.acquire()
    print("user {} : 抢到面了".format(name))
    fork_lock.acquire()
    print("user {} : 抢到叉子了".format(name))
    print("user {} -> 用叉子吃面啦！！！！".format(name))
    fork_lock.release()
    print("user {} : 放下叉子，还拿着面".format(name))
    noodle_lock.release()
    print("user {} : 放下叉子和面".format(name))


def eat2(name, noodle_lock, fork_lock):
    fork_lock.acquire()
    print("user {} : 抢到叉子了".format(name))
    noodle_lock.acquire()
    print("user {} : 抢到面了".format(name))
    print("user {} -> 用叉子吃面啦！！！！".format(name))
    noodle_lock.release()
    print("user {} : 放下叉子和面".format(name))
    fork_lock.release()
    print("user {} : 放下叉子，还拿着面".format(name))


if __name__ == '__main__':
    fork_lock=noodle_lock = Lock()
    t_list = []
    func_list = [eat1] * 20 + [eat2] * 20
    for i in range(len(func_list)):
        t = Thread(target=func_list[i], args=(i, noodle_lock, fork_lock))
        t_list.append(t)
    for t in t_list:
        t.start()
