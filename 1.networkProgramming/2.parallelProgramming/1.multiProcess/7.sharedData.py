from multiprocessing import Process, Lock, Manager

"""
通过Manger可以让数据再各进程中共享
"""
def change_dict(dict, lock):
    with lock:
        dict['count'] -= 1


if __name__ == '__main__':
    # Manager能让数据在各进程之间共享
    with Manager() as m:
        dt = m.dict({'count': 1000})
        lock = Lock()
        p_list = []
        for i in range(100):
            p = Process(target=change_dict, args=(dt, lock))
            p.start()
            p_list.append(p)
        for p in p_list: p.join()
        print(dt)
