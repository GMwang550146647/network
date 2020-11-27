import queue

"""
数据安全的队列，不用加锁
    queue.Queue(size)
    
"""


def func1(size=5, addition=0):
    """
    超过其大小就会锁死
    """
    q = queue.Queue(size)
    for i in range(size + addition):
        q.put(i)
        print("fun1 put {} in queue".format(i))
    for i in range(size + addition):
        print("fun1 get {} in queue".format(q.get()))


def func2(size=5):
    """
    令其超过大小的时候报错
    """
    q = queue.Queue(size)
    for i in range(size + 1):
        try:
            q.put_nowait(i)
            print("fun1 put {} in queue".format(i))
        except queue.Full as err:
            print("queue full, can't put {} in queue. {}".format(i, err))
    for i in range(size + 1):
        try:
            print("fun1 get {} in queue".format(q.get_nowait()))
        except queue.Empty as err:
            print("queue empty, can't get {} from queue. {}".format(i, err))


def func3():
    """
    无限大的队列
    """
    q = queue.Queue()
    for i in range(10000000):
        try:
            q.put_nowait(i)
            print("fun1 put {} in queue".format(i))
        except queue.Full as err:
            print("queue full, can't put {} in queue. {}".format(i, err))
    for i in range(10000000):
        try:
            print("fun1 get {} in queue".format(q.get_nowait()))
        except queue.Empty as err:
            print("queue empty, can't get {} from queue. {}".format(i, err))


if __name__ == '__main__':
    # func2(5)
    # func1(5,addition=1)
    func3()
