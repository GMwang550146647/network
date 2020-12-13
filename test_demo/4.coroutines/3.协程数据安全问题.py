import asyncio
import time
from threading import Thread

"""
要使用await ，就要用async
    await 后面接的一定要是asyncio中写好的阻塞方法
"""

def time_it(func, args):
    now = time.time()
    func(**args)
    return round((time.time() - now)*1000,3)

class AsyncioRun():
    def __init__(self):
        self.a = 0

    async def add(self):
        for i in range(300000):
            # await asyncio.sleep(0.00000001)
            self.a += 1

    async def sub(self):
        for i in range(300000):
            # await asyncio.sleep(0.00000001)
            self.a -= 1

    def run(self, n_coroutines=5):
        tasks = [self.add] * n_coroutines + [self.sub] * n_coroutines
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.wait(
                [taski() for taski in tasks]
            )
        )
        print("AsyncioRun Resutl: {}".format(self.a))


class ThreadRun():
    def __init__(self):
        self.a = 0

    def add(self):
        for i in range(3000000):
            self.a += 1

    def sub(self):
        for i in range(3000000):
            self.a -= 1

    def run(self, n_threads=5):
        tasks = [self.add] * n_threads + [self.sub] * n_threads
        tasks = [Thread(target=taski) for taski in tasks]
        for taski in tasks: taski.start()
        for taski in tasks: taski.join()
        print("ThreadRun Result: {}".format(self.a))


if __name__ == '__main__':
    # 1.是否数据安全呢？
    t1=time_it(AsyncioRun().run,{'n_coroutines':2})
    t2=time_it(ThreadRun().run,{'n_threads':2})
    print("AsyncioRun: {}ms".format(t1))
    print("ThreadRun: {}ms".format(t2))
