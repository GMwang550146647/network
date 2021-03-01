import asyncio
import requests
import os
import time

"""
注意：
    这个完全没有实现同时性
"""


async def get_html(url):
    print(f'{url} begins')
    t1 = time.time()
    # time.sleep(0.3)  #阻塞的时候不调用下一个协程
    await asyncio.sleep(0.2)  # 阻塞的时候会调用下一个协程
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    }
    html = requests.get(url, headers=headers).text
    with open(os.path.join('download', f'7.0.0.{url.split(".")[1]}.html'), 'w') as f:
        f.write(html)
    print(f'{url} ends: Used {time.time() - t1}s')
    return url, html


async def callback(task):
    print("I am callback and {}".format(task.result[0]))
    with open(os.path.join('download', f'7.0.1.{task.result[0].split(".")[1]}.html'), 'w') as f:
        f.write(task.result[1])


def fun1():
    t1 = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html(host) for host in ['http://www.sina.com.cn', 'http://www.sohu.com', 'http://www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))  # 挂起操作需要手动指定（如果只有一个任务的时候，不用wait）
    loop.close()
    print(f"Total time: {time.time() - t1}")


def fun2():
    """
    用task对象可以添加回调函数
    :return:
    """
    t1 = time.time()
    loop = asyncio.get_event_loop()
    tasks = []
    for host in ['http://www.sina.com.cn', 'http://www.sohu.com', 'http://www.163.com']:
        task = asyncio.ensure_future(get_html(host))
        task.add_done_callback(callback)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(f"Total time: {time.time() - t1}")


if __name__ == '__main__':
    # fun1()
    fun2()
