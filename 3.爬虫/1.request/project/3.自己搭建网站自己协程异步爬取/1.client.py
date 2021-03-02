import aiohttp
import asyncio
import time
from lxml import etree

t1 = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/gmwang',
    'http://127.0.0.1:5000/feifei',
]


async def get_request(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url) as response:
            page_text = await response.text()
            # print(page_text)
            return page_text


def parse(task):
    tree = etree.HTML(task.result())
    result = tree.xpath('//div/text()')[0]
    print(result)


tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print("Total_time:{}".format(time.time() - t1))
