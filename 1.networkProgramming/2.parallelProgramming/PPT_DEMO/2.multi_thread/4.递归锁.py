"""
递归锁 recursion Lock
    特点： 1.同一个锁在同一线程可以被锁多次,但是同样要解锁同样次数，不然就会死锁
          2.效率比mutexLock低
          3.递归锁能解决互斥锁死锁现象！
"""

# from threading import RLock as Lock, Thread # RLock
from threading import Lock, Thread  # Lock






def lock_twice(i, lock):
    lock.acquire()
    lock.acquire()
    print("{} lock_twice :Start".format(i))
    lock.release()
    lock.release()
    print("{} lock_twice :End".format(i))


def lock_once(i, lock):
    lock.acquire()
    print("{} lock_once: Start".format(i))
    lock.release()
    print("{} lock_once: End".format(i))


def lock_twice_release_once(i, lock):
    lock.acquire()
    lock.acquire()
    print("{} lock_twice_release_once :Start".format(i))
    lock.release()
    print("{} lock_twice_release_once :End".format(i))

def multi_thread(target,n_threads=5):
    lock = Lock()
    t_list=[]
    for i in range(n_threads):
        ti=Thread(target=target, args=(i,lock))
        ti.start()
        t_list.append(ti)
    for ti in t_list: ti.join()

if __name__ == '__main__':
    lock = Lock()
    # 1.上锁一次，释放一次
    multi_thread(target=lock_once)
    print("________________THIS IS A SEPARATION LINE________________")
    # 2.上锁两次，释放两次（如果是Lock(),他把锁拿到了，再等待一次锁，就会死锁；如果是RLock,锁两次要解两次才行)
    multi_thread(target=lock_twice)
    print("________________THIS IS A SEPARATION LINE________________")
    # 3.上锁两次，释放一次，会卡住，因为还有一重锁没有解，其他线程不能获取锁
    multi_thread(target=lock_twice_release_once)
