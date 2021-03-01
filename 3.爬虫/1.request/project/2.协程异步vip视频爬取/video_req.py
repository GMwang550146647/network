import time
import os
import requests
from datetime import datetime

download_dir = 'download'
os.makedirs(download_dir, exist_ok=True)


def post_request(url, data=None, headers=None,name='download.html'):
    response=requests.post(url=url, data=data,headers=headers)
    html =response.text
    with open(os.path.join(download_dir, name), 'w') as f:
        f.write(html)
    print(f'{url} ends: Used {time.time() - t1}s')
    return html


t1 = time.time()
tasks = []
url = 'https://api.52wyb.com/action/playinfo'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Referer': 'https://api.52wyb.com/',
    'Origin': 'https://api.52wyb.com'
}

import time
# 当前日期和时间
print(time.time())
time_details1=[4843751747,1614592796.349173]
time_details2=[4843752056,1614592898.922615]
print(time_details1[0]-time_details2[0])
print(time_details1[1]-time_details2[1])
tm=round((time.time()-time_details1[1])*3+time_details1[0])

data = [
    {
        'v': 'https://www.iqiyi.com/v_1ihkivfj14k.html?vfm=2008_aldbd',
        'sver':'2.3',
        'cip':'17.87.76.234',
        'cip_hex':"11574cea",
        'csign':'addc1842b54f3568caec615c8cef6aa4',
        'tm':tm,
        'from':'http://www.cdcer.net/',
        'ep':'e5f90143e82b6090c4c88a66d7bbf18df4acb6048691486fb5a35cb10702e5b9cec2827e44560b9f0c829eac4d66b842377305687a06d00d89b0af80e7624498a31d6ee514751de0afd619cf6ec8dc0322b8875b6f1628912e045f1c0067686e970c46e5784b6bc99075d7fd6bb6db5b',
        # ''

    },
]

for i, data_i in enumerate(data):
    c = post_request(url, data_i,headers)
    print(c)
print(f'Total time: {time.time() - t1}s')
