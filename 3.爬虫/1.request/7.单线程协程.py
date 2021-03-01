import asyncio
import requests
async def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    }
    html=requests.get(url,headers=headers).text

    return url,html
def callback(task):
    print("I am callback and {}".format(task.result[0]))
    with open(f'{task.result[0]}.html','w') as f:
        f.write(task.result[1])

loop = asyncio.get_event_loop()
tasks = [get_html(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()