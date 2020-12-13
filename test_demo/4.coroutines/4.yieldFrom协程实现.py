import time
import asyncio
import random
from threading import current_thread

def time_it(func, args):
    now = time.time()
    func(**args)
    return round((time.time() - now)*1000,3)
class AsyncioRun():
    def __init__(self):
        self.p = []

    async def func(self, t, ith):
        print("Start : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))
        await asyncio.sleep(t)
        self.p.append(round(t * 1000, 2))
        print("End : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))

    def run(self, n_tasks=5):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.wait(
                [self.func(random.random(), ith) for ith in range(n_tasks)]
            )
        )
        print("AsyncioRun Result: {}".format(self.p))


class MyCoroutineRun():
    def __init__(self):
        self.p = []

    def run(self, n_tasks=10):
        """
        不是真正睡各自的时间，只是把最长的那个睡眠时间记录起来，然后让逐个较短时间的任务先去各自完成，给人的错觉是同时执行
            例如：
                a任务要睡3s，b任务要睡4s，他们共同睡的3s可以由a任务执行，然后b任务多出来的1s让其自己睡就好了，
                这样完成这两个时间的总时长是4s不是7s
        :param n_paral:
        :return:
        """

        def sleep_assist(t):
            yield time.time() + t

        def sleep(t, ith):
            print("Start : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))
            g = sleep_assist(t)
            yield from g
            self.p.append(round(t * 1000, 2))
            print("End : Thread {} received task {} -> {}ms".format(current_thread().ident % 100, ith, t * 1000))

        g_list = [sleep(random.random(), i) for i in range(n_tasks)]
        time_list = [next(gi) for gi in g_list]
        time_dict = {item[0]: item[1] for item in zip(time_list, g_list)}
        while time_dict:
            min_time = min(time_dict)
            time.sleep(min_time - time.time())
            try:
                next(time_dict[min_time])
            except StopIteration:
                pass
            del time_dict[min_time]
        print("MyCoroutineRun Result: {}".format(self.p))


if __name__ == '__main__':
    t1=time_it(AsyncioRun().run,{"n_tasks":5})
    print("AsyncioRun Time : {} ms".format(t1))
    print("________________THIS IS A SEPARATION LINE________________")
    t2=time_it(MyCoroutineRun().run, {"n_tasks": 5})
    print("MyCoroutineRun Time : {} ms".format(t2))

