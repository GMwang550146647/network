import requests
import datetime
proxy_list = [{'http:': 'http://59.125.123.129:81'}, {'http:': 'http://42.238.80.165:9999'},
              {'http:': 'http://175.42.68.225:9999'},{'http:': 'http://115.221.245.70:9999'},
              {'http:': 'http://120.83.107.26:9999'}, {'http:': 'http://60.176.121.79:8888'},
              {'http:': 'http://120.83.109.100:9999'}]
url = 'https://gwgp-kk6owjrbujz.i.bdcloudapi.com/aladdin/ip/query'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'timestamp': '{}T09:32:25Z@4d0d39614f3dea35dbaa9ba4750891e3'
}
for ip_i in proxy_list:
    result_ip = requests.get(url, headers=headers, proxies=ip_i).json()
    print(f'{ip_i}: {result_ip}')
