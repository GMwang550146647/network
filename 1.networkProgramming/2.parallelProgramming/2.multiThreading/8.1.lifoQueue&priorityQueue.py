from queue import Queue,LifoQueue,PriorityQueue
import queue
"""
LifoQueue
    栈:后进先出
PriorityQueue
    队列:优先级队列
"""
def lifo_queue():
    """
    后进先出（栈）
    """
    q = LifoQueue()
    for i in range(5):
        try:
            q.put_nowait(i)
            print("fun1 put {} in queue".format(i))
        except queue.Full as err:
            print("queue full, can't put {} in queue. {}".format(i, err))
    for i in range(5):
        try:
            print("fun1 get {} in queue".format(q.get_nowait()))
        except queue.Empty as err:
            print("queue empty, can't get {} from queue. {}".format(i, err))

def priority_queue():
    """
    优先级队列
        数字越低，优先级越大
    """
    q = PriorityQueue()
    for i in range(5,-1,-1):
        try:
            q.put_nowait((i,i))
            print("fun1 put {} in queue".format(i))
        except queue.Full as err:
            print("queue full, can't put {} in queue. {}".format(i, err))
    for i in range(5):
        try:
            print("fun1 get {} in queue".format(q.get_nowait()))
        except queue.Empty as err:
            print("queue empty, can't get {} from queue. {}".format(i, err))
if __name__ == '__main__':
    lifo_queue()
    priority_queue()
