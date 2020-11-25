"""
生产者消费者模型
    #爬虫
    #分布式操作
    #本质：让生产者数据和消费者数据的效率达到平衡并且效益最大化
"""
import time
from multiprocessing import Queue,Process
def consumer(q,ith):
    count=0
    while True:
        count+=1
        print("Consumer {} -> {}th get: receive from consumer {}".format(ith,count, q.get()))
        time.sleep(10)
def producer(q,ith):
    count=0
    while True:
        count+=1
        q.put(ith)
        print("Producer {} -> {}th put: send my id {}".format(ith,count, ith))
        time.sleep(2)
if __name__ == '__main__':
    n_consumer=8
    n_producer=2
    q=Queue()
    for i in range(n_consumer):
        ci=Process(target=consumer,args=(q,i+1,))
        ci.start()
    for j in range(n_producer):
        pi=Process(target=producer,args=(q,j+1,))
        pi.start()