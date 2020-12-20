import asyncio
from threading import current_thread, Thread
import random
import time

"""
要使用await ，就要用async
    await 后面接的一定要是asyncio中写好的阻塞方法
"""


class AsyncioRun():
    def __init__(self):
        self.p = []

    async def func(self, t, ith, task_load):
        print("Start : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))
        k = 0
        for i in range(task_load):
            k += 1
        await asyncio.sleep(t)
        self.p.append(round(t * 1000, 2))
        print("End : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))

    def run(self, task_load):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.wait(
                [self.func(random.random(), ith, task_load[ith]) for ith in range(len(task_load))]
            )
        )
        print("AsyncioRun Result: {}".format(self.p))


class ThreadRun():
    def __init__(self):
        self.p = []

    def func(self, t, ith, task_load):
        print("Start : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))
        k = 0
        for i in range(task_load):
            k += 1
        time.sleep(t)
        self.p.append(round(t * 1000, 2))
        print("End : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))

    def run(self, task_load):
        t_list=[]
        for ith,task_loadi in enumerate(task_load):
            ti=Thread(target=self.func,args=(random.random(), ith, task_load[ith]))
            ti.start()
            t_list.append(ti)
        for ti in t_list: ti.join()
        print("ThreadRun Result: {}".format(self.p))

if __name__ == '__main__':
    # 1.单线程并行多任务，先完成先返回
    task_load = [1, 2, 3000000000, 4]
    # ThreadRun().run(task_load)
    AsyncioRun().run(task_load)
