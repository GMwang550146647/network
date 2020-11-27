from multiprocessing import Process, Queue, Lock
import requests
import os


def consumer(name, q, dir):
    while True:
        tup = q.get()
        if tup == None: break
        print("Consumer {}  write {}".format(name, tup[0]))
        with open(os.path.join(dir, "{}.html".format(tup[0])), mode='w', encoding='utf-8') as f:
            f.write(tup[1])


def producer(name, task, url, q):
    ret = requests.get(url)
    print("Producer {}  search {}".format(name, task))
    q.put((task, ret.text))


if __name__ == '__main__':
    url_dict = {
        'baidu': "http://www.baidu.com",
        'bili': "https://www.bilibili.com",
        'aiqiyi': 'https://www.iqiyi.com',
        'google': 'https://www.google.com.hk/webhp?hl=zh-CN&sourceid=cnhp',
    }
    dir = "data"
    os.makedirs(dir, exist_ok=True)

    q = Queue()
    producer_list = []
    for i, (index, url) in enumerate(url_dict.items()):
        pi = Process(target=producer, args=(i, index, url, q,))
        pi.start()
        producer_list.append(pi)
    n_consumer = 2
    consumer_list = []
    for i in range(n_consumer):
        pi = Process(target=consumer, args=(i, q, dir))
        pi.start()
        consumer_list.append(pi)
    # 等待producer都结束，异步阻塞
    [pi.join() for pi in producer_list]
    # 让consumer都结束
    [q.put(None) for i in range(len(consumer_list))]
