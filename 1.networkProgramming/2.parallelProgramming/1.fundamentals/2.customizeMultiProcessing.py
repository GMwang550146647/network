import os
import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, argv):
        super().__init__()
        self.argv = argv

    def run(self):
        time.sleep(1)
        print("ppid:{}\tpid:{}\tparams:{}".format(os.getppid(), os.getpid(), self.argv))


if __name__ == '__main__':
    print('-->{}'.format(os.getpid()))
    p=MyProcess('gmwang')
    p.start()
    #强制终止
    p.terminate()
    #发信息过去，但是尚未终止
    print(p.is_alive())
    time.sleep(0.01)
    #终止了
    print(p.is_alive())


