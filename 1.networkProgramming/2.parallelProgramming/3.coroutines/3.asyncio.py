import asyncio

"""
要使用await ，就要用async
    await 后面接的一定要是asyncio中写好的阻塞方法
"""
async def func(name,i):
    print("start -> name:{}  -> {} th".format(name,i))
    await asyncio.sleep(1)
    print("end -> name:{}  -> {} th".format(name,i))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait(
            [func('gmwang',i) for i in range(10)]
        )
    )
