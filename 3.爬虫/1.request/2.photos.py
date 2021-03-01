import requests
import os

photo_url ='https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1842162006,830554131&fm=26&gp=0.jpg'
save_file=os.path.join('download','{}.img.jpg')
#1.requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'
}
img_data = requests.get(photo_url, headers=headers).content
with open(save_file.format(1),'wb') as f:
    f.write(img_data)


# 2.urllib
from urllib import request
request.urlretrieve(photo_url,filename=save_file.format(2))
