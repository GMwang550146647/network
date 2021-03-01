"""
1.反爬机制
    1.反爬文件：
        url/robots.txt
    2.UA检查

"""
import os
import requests

urls = {
    'sogou': {
        'url': 'https://www.sogou.com/web',
        'params': {
            'query': 'gmwang'
        },
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'
        }
    }
}
for namei, args in urls.items():
    response = requests.get(args['url'], params=args['params'],headers=args['headers'])
    content = response.text
    save_file = os.path.join('download', f'{namei}.html')
    with open(save_file, 'w') as f:
        f.write(content)
