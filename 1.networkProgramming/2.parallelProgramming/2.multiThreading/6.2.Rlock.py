from threading import Lock,RLock,Thread

def recur_lock():
    l = RLock()
    l.acquire()
    l.acquire()
    print("希望被锁住的代码")
    l.release()
    l.release()
if __name__ == '__main__':
    for i in range(5):
