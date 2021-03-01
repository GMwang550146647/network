import aiohttp
import asyncio
import time
import os

download_dir = 'download'
os.makedirs(download_dir,exist_ok=True)


async def request(url, methods='get', data=None, name='download.html'):
    async with aiohttp.ClientSession() as s:
        async with getattr(s, methods)(url=url, data=data) as response:
            html = await response.text()
    with open(os.path.join(download_dir, name), 'w') as f:
        f.write(html)
    print(f'{url} ends: Used {time.time() - t1}s')
    return html


t1 = time.time()
tasks = []
url = 'https://api.52wyb.com/action/playinfo?sver=2.3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Referer':'https://api.52wyb.com/',
    'Origin':'https://api.52wyb.com'
}
data = [
    {'v': 'https://www.iqiyi.com/v_1ihkivfj14k.html?vfm=2008_aldbd'},
]

loop = asyncio.get_event_loop()
for i, data_i in enumerate(data):
    c = request(url, 'post')
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop.run_until_complete(asyncio.gather(*tasks))
print(f'Total time: {time.time() - t1}s')
