from threading import Thread, Lock, RLock

"""
死锁出现的核心原因
    多把锁，多个线程之间，交叉使用
死锁原因
    eat1 与eat2 拿面和叉子的顺序不一样，最后一个人拿着叉子，一个人拿着面，就死锁了

解决方法：
    把所有的锁弄成一把递归锁，但是锁多次就行了
"""


class RecursiveLock():
    def eat1(self, name, noodle_lock, fork_lock):
        noodle_lock.acquire()
        print("user {} : 抢到面了".format(name))
        fork_lock.acquire()
        print("user {} : 抢到叉子了".format(name))
        print("user {} -> 用叉子吃面啦！！！！".format(name))
        fork_lock.release()
        print("user {} : 放下叉子，还拿着面".format(name))
        noodle_lock.release()
        print("user {} : 放下叉子和面".format(name))

    def eat2(self, name, noodle_lock, fork_lock):
        fork_lock.acquire()
        print("user {} : 抢到叉子了".format(name))
        noodle_lock.acquire()
        print("user {} : 抢到面了".format(name))
        print("user {} -> 用叉子吃面啦！！！！".format(name))
        noodle_lock.release()
        print("user {} : 放下叉子和面".format(name))
        fork_lock.release()
        print("user {} : 放下叉子，还拿着面".format(name))

    def run_two_mutex_lock(self, n_threads=10):
        noodle_lock = Lock()
        fork_lock = Lock()
        t_list = []
        func_list = [self.eat1] * n_threads + [self.eat2] * n_threads
        for i in range(len(func_list)):
            t = Thread(target=func_list[i], args=(i, noodle_lock, fork_lock))
            t_list.append(t)
        for t in t_list:
            t.start()

    def run_RLock(self, n_threads=10):
        noodle_lock = fork_lock = RLock()
        t_list = []
        func_list = [self.eat1] * n_threads + [self.eat2] * n_threads
        for i in range(len(func_list)):
            t = Thread(target=func_list[i], args=(i, noodle_lock, fork_lock))
            t_list.append(t)
        for t in t_list:
            t.start()


if __name__ == '__main__':
    # 1.递归锁解决死锁
    RecursiveLock().run_RLock()
    print("________________THIS IS A SEPARATION LINE________________")
    # 2.死锁
    RecursiveLock().run_two_mutex_lock()
