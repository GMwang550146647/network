import aiohttp
import asyncio
import time
import os
async def get_request(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url=url) as response:
            html=await response.text()
    with open(os.path.join('download', f'7.1.{url.split(".")[1]}.html'), 'w') as f:
        f.write(html)
    print(f'{url} ends: Used {time.time() - t1}s')
    return html

t1=time.time()
tasks=[]
urls=['http://www.sina.com.cn', 'http://www.sohu.com', 'http://www.163.com']
loop = asyncio.get_event_loop()
for url in urls:
    c=get_request(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)
loop.run_until_complete(asyncio.gather(*tasks))
print(f'Total time: {time.time() - t1}s')