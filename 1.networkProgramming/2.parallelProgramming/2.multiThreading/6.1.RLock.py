from threading import RLock, Thread
import time
import  sys
sys.setrecursionlimit(1000000)
# from multiprocessing import Process as Thread

a = 8100


def run_RLock(n_threads=90):
    def thread_run_RLock(rlock, n_threads=90):
        with rlock:
            t_list = []
            for i in range(n_threads):
                print("here{}".format(i))
                ti = Thread(target=thread_thread_run_RLock, args=(rlock,))
                ti.start()
                t_list.append(ti)
            for ti in t_list: ti.join()

    def thread_thread_run_RLock(rlock):
        global a
        with rlock:
            print("here")
            time.sleep(0.000001)
            a -= 1

    global a
    t_list = []
    n_sub_thread = 10
    tempt_a = a
    rlock = RLock()
    for i in range(n_threads):
        ti = Thread(target=thread_run_RLock, args=(rlock, n_sub_thread))
        ti.start()
        t_list.append(ti)
    for ti in t_list: ti.join()
    print("After total {} times ,Reduce from {} to {}".format(n_threads * n_sub_thread, tempt_a, a))


def run(n_threads=10):
    def thread_run(r_lock,n_threads=10):
        t_list = []
        for i in range(n_threads):
            ti = Thread(target=thread_thread_run_RLock)
            ti.start()
            t_list.append(ti)
        for ti in t_list: ti.join()

    def thread_thread_run_RLock():
        global a
        time.sleep(0.000001)
        a -= 1

    global a
    t_list = []
    n_sub_thread = 10
    tempt_a = a
    rlock = RLock()
    for i in range(n_threads):
        ti = Thread(target=thread_run, args=(n_sub_thread,rlock))
        ti.start()
        t_list.append(ti)
    for ti in t_list: ti.join()
    print("After total {} times ,Reduce from {} to {}".format(n_threads * n_sub_thread, tempt_a, a))


if __name__ == '__main__':
    # run()
    run_RLock()
