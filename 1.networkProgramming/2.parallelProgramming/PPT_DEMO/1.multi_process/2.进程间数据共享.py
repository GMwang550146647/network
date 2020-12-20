from multiprocessing import Process, Lock, Manager, Queue, Value
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
            with open("2.shared_data.txt") as f:
                content = f.read()
            time.sleep(0.001)
            ticket = int(content) - 1
            with open("2.shared_data.txt", 'w') as f:
                f.write(str(ticket))

    def get_ticket(self):
        content = ''
        while content == "":
            with open("2.shared_data.txt") as f:
                content = f.read()
        time.sleep(0.001)
        ticket = int(content) - 1
        with open("2.shared_data.txt", 'w') as f:
            f.write(str(ticket))

    def buy_ticket_multi_lock(self, n=100):
        n_tickets = self.search_ticket()
        lock = Lock()
        p_list = []
        for i in range(n):
            p = Process(target=self.get_ticket_lock, args=(lock,))
            p.start()
            p_list.append(p)
        [p.join() for p in p_list]
        n_tickets_now = self.search_ticket()
        print("ShareDataUsingFile With Lock: After Buy {} times-> Reduce from {} to {} -> {}"
              .format(n, n_tickets, n_tickets_now, n_tickets - n_tickets_now))

    def buy_ticket_multi(self, n=100):
        n_tickets = self.search_ticket()
        p_list = []
        for i in range(n):
            p = Process(target=self.get_ticket)
            p.start()
            p_list.append(p)
        [p.join() for p in p_list]
        n_tickets_now = self.search_ticket()
        print("ShareDataUsingFile No Lock: After Buy {} times-> Reduce from {} to {} -> {}"
              .format(n, n_tickets, n_tickets_now, n_tickets - n_tickets_now))

    def run(self, n=100):
        self.buy_ticket_multi(n)
        self.buy_ticket_multi_lock(n)


class ShareDataUsingManager():
    """
    2.通过Manger可以让数据在各进程中共享
    """

    def shared_data_lock(self, n=100):
        def change_dict_lock(dict, lock):
            with lock:
                dict['count'] -= 1

        # Manager能让数据在各进程之间共享
        with Manager() as m:
            dt = m.dict({'count': 100})
            dt_tempt = dt['count']
            lock = Lock()
            p_list = []
            for i in range(n):
                p = Process(target=change_dict_lock, args=(dt, lock))
                p.start()
                p_list.append(p)
            for p in p_list: p.join()
            print("ShareDataUsingManager With lock: Reduce from 100 to {} -> {}".format(dt['count'],
                                                                                        dt_tempt - dt['count']))

    def shared_data(self, n=100):
        def change_dict(dict):
            dict['count'] -= 1

        # Manager能让数据在各进程之间共享
        with Manager() as m:
            dt = m.dict({'count': 100})
            dt_tempt = dt['count']
            p_list = []
            for i in range(n):
                p = Process(target=change_dict, args=(dt,))
                p.start()
                p_list.append(p)
            for p in p_list: p.join()
            print("ShareDataUsingManager No lock: Reduce from 100 to {} -> {}".format(dt['count'],
                                                                                      dt_tempt - dt['count']))

    def run(self, n=100):
        self.shared_data(n)
        self.shared_data_lock(n)


class ShareDataUsingQueue():
    def __init__(self):
        self.queue = Queue()
        self.count = 100
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
        result = self.queue.get()
        print("ShareDataUsingQueue No lock: After {} times Reduce from {} to {} ->{}".format(n, self.count,
                                                                                             result,
                                                                                             self.count - result))

    def run(self, n=100):
        self.share_data(n)


class ShareDataUsingMemory():

    def do_work(self, a):
        a.value -= 1

    def do_mess_work(self, a):
        for i in range(10000):
            a.value -= 1

    def run(self, n=100, mess=False):
        tempt = 100
        a = Value('i', tempt)
        p_list = []
        for i in range(n):
            p = Process(target=self.do_mess_work if mess else self.do_work, args=(a,))
            p.start()
            p_list.append(p)
        for p in p_list: p.join()
        print("ShareDataUsingMemory No lock: After {} times Reduce from {} to {} ->{}".format(n, tempt, a.value,
                                                                                              tempt - a.value))
        return a.value


if __name__ == '__main__':
    # 1.FileSystem
    ShareDataUsingFile().run(n=100)
    print("________________THIS IS A SEPARATION LINE________________")
    # 2.Manager
    ShareDataUsingManager().run(n=100)
    print("________________THIS IS A SEPARATION LINE________________")
    # 3.Queue
    ShareDataUsingQueue().run(n=100)
    print("________________THIS IS A SEPARATION LINE________________")
    # 4.1.Shared Memory: 不会出错，只能代表他太快了,还没经历轮转就做完了
    ShareDataUsingMemory().run(n=100)
    # 4.2.Shared Memory: 把任务增多就会出错了
    ShareDataUsingMemory().run(n=100, mess=True)

    # 5.sleep一下 -> 尝试kill一下
    time.sleep(10000)
