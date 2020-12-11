"""
池
    程序还没开始的时候，还没提交任务，先创建几个线程或者进程
为什么要用池
    先开好，有任务的时候就能直接使用了（开的时候浪费时间）
    开好的线程或者进程一直在池中，可以反复使用，极大减少 开启/关闭/调度线程(进程)的时间开销
    池中的线程(进程)个数决定了操作系统需要调度的任务个数，控制池中的单位
        有利于提高操作系统的效率，减轻操作系统负担

历史
    threading 模块  没有提供池
    multiprocessing 模块 仿照threading写的 有Pool
    concurrent.futures模块 线程池，进程池都能使用相似的方式开启/关闭
基本功能
    submit(fn，*args,**kwargs) 提交任务
    map(func)                  取代for循环的submit操作
    shutdown(wait=True)        pool.close()+pool.join()
    result(timeout=None)       获取结果
    add_done_callback(fn)      回调函数
    done()                     判断是否完成
    cancle()                   取消某任务

重大特点
    返回的数据是按顺序的，非常整齐
"""
# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor as ThreadPoolExecutor
from threading import current_thread, Thread
from multiprocessing import Queue
import time
import random

def time_it(func, args):
    now = time.time()
    func(**args)
    return time.time() - now

class ThreadPoolRun():
    def __init__(self):
        pass

    def thread_task_map(self, kwargs):
        t = kwargs.get("t", None)
        t = round(t if t is not None else random.random(), 1)
        id = kwargs.get("task_id", -1)
        time.sleep(t)
        print("thread {}: task {} sleep for {} s and  ends".format(current_thread().ident % 100, id, t))
        return {id: t}

    def run(self, n_threads=4, n_tasks=20, t=None):
        tp = ThreadPoolExecutor(n_threads)
        # 异步阻塞
        result = [item for item in
                  tp.map(self.thread_task_map, [{"task_id": i, 't': t} for i in range(n_tasks)])]
        print("ThreadPoolRun : {}".format(result))
        return result


class ThreadRun():
    def __init__(self):
        self.queue = Queue()
        self.result = []

    def thread_task(self):
        while True:
            kwargs=self.queue.get()
            if kwargs is None:
                break
            else:
                t = kwargs.get("t", None)
                t = round(t if t is not None else random.random(), 1)
                id = kwargs.get("task_id", -1)
                time.sleep(t)
                print("thread {}: task {} sleep for {} s and  ends".format(current_thread().ident % 100, id, t))
                self.result.append( {id: t})

    def run(self, n_threads=4, n_tasks=20, t=None):
        for i in range(n_tasks):
            self.queue.put({"task_id": i, 't': t})
        for i in range(n_threads):
            self.queue.put(None)
        t_list = []
        for i in range(n_threads):
            ti = Thread(target=self.thread_task)
            ti.start()
            t_list.append(ti)
        for ti in t_list: ti.join()
        print("ThreadRun : {}".format(self.result))
        return self.result


if __name__ == '__main__':
    #1.每次只有n_thread 个工人在干活
    # ThreadPoolRun().run(n_threads=2, n_tasks=10, t=1)

    #2.正序与乱序返回
    t1=time_it(ThreadPoolRun().run,{'n_threads':200,'n_tasks':1000})
    t2=time_it(ThreadRun().run,{'n_threads':200,'n_tasks':1000})
    print("ThreadPoolRun: {} s".format(t1))
    print("ThreadRun: {} s".format(t2))
