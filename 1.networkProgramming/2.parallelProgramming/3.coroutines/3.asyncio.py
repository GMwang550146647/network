import asyncio
from threading import current_thread
import random
"""
要使用await ，就要用async
    await 后面接的一定要是asyncio中写好的阻塞方法
"""
class AsyncioRun():

    async def func(self,t,ith):
        print("Start : Thread {} received task {} -> {}ms".format(current_thread().ident%100,ith,t*1000))
        await asyncio.sleep(t)
        print("End : Thread {} received task {} -> {}ms".format(current_thread().ident%100,ith,t*1000))
    def run(self,n_tasks=5):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.wait(
                [self.func(random.random(), ith) for ith in range(n_tasks)]
            )
        )
if __name__ == '__main__':
    AsyncioRun().run()
