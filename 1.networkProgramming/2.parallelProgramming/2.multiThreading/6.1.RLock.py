"""
递归锁 recursion Lock
    特点： 同一个锁在同一线程可以被锁多次
          效率比mutexLock低
"""
from threading import RLock as Lock,Thread
from threading import Lock,Thread
def lock_twice(i,lock):
    lock.acquire()
    lock.acquire()
    print("{}:Start".format(i))
    lock.release()
    lock.release()
    print("{}:End".format(i))


def lock_once(lock):
    lock.acquire()
    print("Start")
    lock.release()
    print("End")
if __name__ == '__main__':
    for i in range(5):
        Thread(target=lock_twice,args=)
    # mutex_lock()
