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
def process_task(info, task_id):
    print("Process {}: task {} received {} -> start".format(os.getpid(), task_id, info))
    time.sleep(0.5)
    print("Process {}:  end".format(os.getpid()))
    return task_id


def multi_process(n_process=4, n_tasks=20):
    pp = ProcessPoolExecutor(n_process)
    future_l = []
    for i in range(n_tasks):
        # 以下三种方式都合法
        # tp.submit(process_task,task_id=i,info='gmwang')
        # tp.submit(process_task,'gmwang',i)
        ppi = pp.submit(process_task, 'gmwang', task_id=i)
        future_l.append(ppi)
    # 异步非阻塞
    result = [ppi.result() for ppi in future_l]
    return result


"""
2.线程（进程）启动方式2 -> map
"""


def process_task_map(kwargs):
    print("Process {}: task {} received {} -> start".format(os.getpid(), kwargs.get("task_id", -1),
                                                            kwargs.get("info", "None")))
    time.sleep(0.5)
    print("Process {}:  end".format(current_thread().ident % 100))
    return kwargs.get("task_id", -1)



def multi_process_map(n_process=4, n_tasks=20):
    pp = ProcessPoolExecutor(n_process)
    result = [item for item in pp.map(process_task_map, [{"info": "gmwang", "task_id": i} for i in range(n_tasks)])]
    return result


if __name__ == '__main__':
    # 1.submit版本
    process_result1 = multi_process(4, 20)
    print(process_result1)
    # 2.map版本
    process_result2 = multi_process_map(4, 20)
    print(process_result2)
