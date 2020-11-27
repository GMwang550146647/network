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
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import time
import os

"""
1.线程（进程）启动方式1 -> submit
"""


def thread_task(info, task_id):
    print(info)
    print("thread {}: task {} received {} -> start".format(current_thread().ident % 100, task_id, info))
    time.sleep(0.5)
    print("thread {}:  end".format(current_thread().ident % 100))
    return task_id


def multi_threading(n_threads=4, n_tasks=20):
    tp = ThreadPoolExecutor(n_threads)
    future_l = []
    for i in range(n_tasks):
        # 以下三种方式都合法
        # tp.submit(thread_task,task_id=i,info='gmwang')
        # tp.submit(thread_task,'gmwang',i)
        tpi = tp.submit(thread_task, 'gmwang', task_id=i)
        future_l.append(tpi)
    # 异步非阻塞
    result = [tpi.result() for tpi in future_l]
    return result

"""
2.线程（进程）启动方式2 -> map
"""


def thread_task_map(kwargs):
    print("thread {}: task {} received {} -> start".format(current_thread().ident % 100, kwargs.get("task_id", -1),
                                                           kwargs.get("info", "None")))
    time.sleep(0.5)
    print("thread {}:  end".format(current_thread().ident % 100))
    return kwargs.get("task_id", -1)



def multi_threading_map(n_threads=4, n_tasks=20):
    tp = ThreadPoolExecutor(n_threads)
    result = [item for item in tp.map(thread_task_map, [{"info": "gmwang", "task_id": i} for i in range(n_tasks)])]
    return result



if __name__ == '__main__':
    # 1.submit版本
    thread_result1 = multi_threading(4, 20)
    print(thread_result1)
    # 2.map版本
    thread_result2 = multi_threading_map(4, 20)
    print(thread_result2)
