from multiprocessing import Process, Lock
import json
import time
"""
进程锁
"""

def search_ticket(i):
    with open("4.shared_data.json") as f:
        ticket = json.load(f)
    print("{}: {} tickets left!".format(i, ticket['count']))


def buy_ticket(i):
    # var = 1 / i #这里是触发错误的地方
    with open("4.shared_data.json") as f:
        ticket = json.load(f)
    if ticket['count'] > 0:
        ticket['count'] -= 1
        print("{}:Ticket got!".format(i))
        time.sleep(0.1)
        with open("4.shared_data.json", 'w') as f:
            json.dump(ticket, f)
    else:
        print("{}:Ticket not found!".format(i))


def get_ticket_lock(i, lock):
    search_ticket(i)
    # 1.加锁,程序出错会自动释放锁
    with lock:
        buy_ticket(i)
    # 2.加锁，不安全，程序出错会一直锁住
    # lock.acquire()
    # buy_ticket(i)
    # lock.release()


def get_ticket(i):
    search_ticket(i)
    buy_ticket(i)


if __name__ == '__main__':

    # 1.不加锁，出现bug
    # for i in range(10):
    #     p = Process(target=get_ticket, args=(i,))
    #     p.start()

    # 2.加锁，无bug
    lock = Lock()
    for i in range(10):
        p = Process(target=get_ticket_lock, args=(i, lock,))
        p.start()
