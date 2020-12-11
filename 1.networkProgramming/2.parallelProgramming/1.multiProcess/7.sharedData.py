from multiprocessing import Process, Lock, Manager

"""
通过Manger可以让数据再各进程中共享
"""


def shared_data_lock():
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
        print(dt)


def shared_data():
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
        print(dt)


if __name__ == '__main__':
    # 1.without lock
    shared_data()
    # 2.lock
    shared_data_lock()
