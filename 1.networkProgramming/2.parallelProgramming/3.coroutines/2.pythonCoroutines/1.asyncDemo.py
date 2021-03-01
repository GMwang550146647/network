import asyncio
import time

"""
有await的函数必须在函数定义前面加上async
"""
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"start as {time.strftime('%X')}")
    await  say_after(1, 'Hello')
    await  say_after(2, 'World')


if __name__ == '__main__':
    asyncio.run(main())
