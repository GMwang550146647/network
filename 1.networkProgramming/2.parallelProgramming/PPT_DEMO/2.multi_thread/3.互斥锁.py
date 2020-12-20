from threading import Thread, Lock
import time


class Run():
    def __init__(self):
        self.a = 0

    def add(self):
        for i in range(300000):
            self.a += 1

    def sub(self):
        for i in range(300000):
            self.a -= 1

    def run(self, n_threads=2):

        add_threads = []
        sub_threads = []
        for i in range(n_threads):
            t1 = Thread(target=self.add)
            t2 = Thread(target=self.sub)
            add_threads.append(t1)
            sub_threads.append(t2)
            t1.start()
            t2.start()
        [ti.join() for ti in add_threads]
        [ti.join() for ti in sub_threads]
        print("Run: {}".format(self.a))


class MutexLockRun():
    def __init__(self):
        self.a = 0
        self.lock = Lock()

    def add(self):
        for i in range(300000):
            with self.lock:
                self.a += 1

    def sub(self):
        for i in range(300000):
            with self.lock:
                self.a -= 1

    def run(self, n_threads=2):
        add_threads = []
        sub_threads = []
        for i in range(n_threads):
            t1 = Thread(target=self.add)
            t2 = Thread(target=self.sub)
            add_threads.append(t1)
            sub_threads.append(t2)
            t1.start()
            t2.start()
        [ti.join() for ti in add_threads]
        [ti.join() for ti in sub_threads]
        print("MutexLockRun: {}".format(self.a))


class RunList():
    def __init__(self):
        self.p = []

    def add(self):
        for i in range(300000):
            self.p.append(1)

    def sub(self):
        for i in range(300000):
            if not self.p:
                time.sleep(0.0000001)  # 强制线程轮转
                # time.sleep(0.0000001)  # 强制线程轮转
            self.p.pop()  # 这里因为有可能两个线程同时pop，但是len(p)==1，这个时候报错，当只有一个线程的时候就不会

    def run(self, n_threads=2):
        add_threads = []
        sub_threads = []
        for i in range(n_threads):
            t2 = Thread(target=self.sub)
            t1 = Thread(target=self.add)
            add_threads.append(t1)
            sub_threads.append(t2)
            t1.start()
            t2.start()
        [ti.join() for ti in add_threads]
        [ti.join() for ti in sub_threads]
        print("RunList: {}".format(self.p))


if __name__ == '__main__':
    #1.a+=1
    Run().run()
    MutexLockRun().run()
    #2.p.append(1)
    RunList().run()
    # 这个RunList()还是会出错
    for i in range(100):
        RunList().run(n_threads=10)
    # MutexLockRunList().run()
