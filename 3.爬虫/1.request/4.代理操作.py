import requests
import datetime
proxy_list = [{'http:': '47.106.162.218:80'}]
url = 'https://gwgp-kk6owjrbujz.i.bdcloudapi.com/aladdin/ip/query'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'timestamp': '2021-03-04T13:58:23Z@432f94a096c26f4b6f623f7657261c5d'
}
for ip_i in proxy_list:
    result_ip = requests.get(url, headers=headers, proxies=ip_i.copy()).json()
    print(f'{ip_i}: {result_ip}')
