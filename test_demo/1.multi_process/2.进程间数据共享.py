from multiprocessing import Process, Lock, Manager, Queue
import json
import time


class ShareDataUsingFile():
    """
    1.通过文件系统可以让数据再各进程中共享（慢）
    """

    def search_ticket(self):
        with open("2.shared_data.txt") as f:
            ticket = int(f.read())
        return ticket

    def get_ticket_lock(self, lock):
        with lock:
            # var = 1 / i #这里是触发错误的地方
            with open("2.shared_data.txt") as f:
                ticket = int(f.read())
            ticket -= 1
            with open("2.shared_data.txt", 'w') as f:
                f.write(str(ticket))

    def get_ticket(self):
        # var = 1 / i #这里是触发错误的地方
        with open("2.shared_data.txt") as f:
            ticket = int(f.read())
        time.sleep(0.1)
        ticket -= 1
        with open("2.shared_data.txt", 'w') as f:
            f.write(str(ticket))

    def buy_ticket_multi_lock(self, n=10):
        n_tickets = self.search_ticket()
        lock = Lock()
        p_list = []
        for i in range(n):
            p = Process(target=self.get_ticket_lock, args=(lock,))
            p.start()
            p_list.append(p)
        [p.join() for p in p_list]
        n_tickets_now = self.search_ticket()
        print("ShareDataUsingFile No Lock: After Buy {} times-> Reduce from {} to {} -> {}"
              .format(n, n_tickets, n_tickets_now, n_tickets - n_tickets_now))

    def buy_ticket_multi(self, n=10):
        n_tickets = self.search_ticket()
        p_list = []
        for i in range(n):
            p = Process(target=self.get_ticket)
            p.start()
            p_list.append(p)
        [p.join() for p in p_list]
        n_tickets_now = self.search_ticket()
        print("ShareDataUsingFile With Lock: After Buy {} times-> Reduce from {} to {} -> {}"
              .format(n, n_tickets, n_tickets_now, n_tickets - n_tickets_now))

    def run(self):
        self.buy_ticket_multi()
        self.buy_ticket_multi_lock()


class ShareDataUsingManager():
    """
    2.通过Manger可以让数据在各进程中共享
    """

    def shared_data_lock(self):
        def change_dict_lock(dict, lock):
            with lock:
                dict['count'] -= 1

        # Manager能让数据在各进程之间共享
        with Manager() as m:
            dt = m.dict({'count': 10000})
            lock = Lock()
            p_list = []
            for i in range(100):
                p = Process(target=change_dict_lock, args=(dt, lock))
                p.start()
                p_list.append(p)
            for p in p_list: p.join()
            print("ShareDataUsingManager With lock: Reduce from 10000 to {}".format(dt['count']))

    def shared_data(self):
        def change_dict(dict):
            dict['count'] -= 1

        # Manager能让数据在各进程之间共享
        with Manager() as m:
            dt = m.dict({'count': 10000})
            p_list = []
            for i in range(100):
                p = Process(target=change_dict, args=(dt,))
                p.start()
                p_list.append(p)
            for p in p_list: p.join()
            print("ShareDataUsingManager No lock: Reduce from 10000 to {}".format(dt['count']))

    def run(self):
        self.shared_data()
        self.shared_data_lock()


class ShareDataUsingQueue():
    def __init__(self):
        self.queue = Queue()
        self.count = 10000
        self.queue.put(self.count)

    def buy_ticket(self, q):
        tickets = q.get()
        q.put(tickets - 1)

    def share_data(self, n=100):
        p_list = []
        for i in range(n):
            p = Process(target=self.buy_ticket, args=(self.queue,))
            p.start()
            p_list.append(p)
        for p in p_list: p.join()
        print("ShareDataUsingManager No lock: After {} times Reduce from {} to {}".format(n, self.count,
                                                                                          self.queue.get()))

    def run(self):
        self.share_data()


if __name__ == '__main__':
    # 1.FileSystem
    ShareDataUsingFile().run()
    # 2.Manager
    ShareDataUsingManager().run()
    # 3.Queue
    ShareDataUsingQueue().run()
