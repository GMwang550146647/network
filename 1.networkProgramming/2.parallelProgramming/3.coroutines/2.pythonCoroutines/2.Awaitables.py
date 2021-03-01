"""
三种 Awaitable Objects
1.Coroutines
2.Tasks
3.Futures
"""
import asyncio
import concurrent.futures

"""
1.Coroutines
async 包装的函数都会转换成一个Coroutines函数，如果没有await，函数不会调用，会返回Coroutines对象
"""


def coroutines():
    """用于直接运行的任务"""

    async def nested():
        return 42

    async def main():
        # Nothing happens if we just call "nested()".
        # A coroutine object is created but not awaited,
        # so it *won't run at all*.
        print(nested())

        # Let's do it differently now and await it:
        print(await nested())  # will print "42".

    asyncio.run(main())


"""
2.Tasks
用于automatically schedule的任务
"""


def tasks():
    async def nested():
        return 42

    async def main():
        # Schedule nested() to run soon concurrently
        # with "main()".
        task = asyncio.create_task(nested())

        # "task" can now be used to cancel "nested()", or
        # can simply be awaited to wait until it is complete:
        await task

    asyncio.run(main())


"""
3.Futures

"""


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)
        print('custom process pool', result)


asyncio.run(main())

if __name__ == '__main__':
    # coroutines()
    # tasks()
    # futures()
    pass
