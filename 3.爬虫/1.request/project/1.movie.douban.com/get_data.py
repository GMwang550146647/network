
import os
import requests
import json

args = {
    'url': 'https://movie.douban.com/j/search_subjects',
    'params': {
        'type': 'movie',
        'page_limit': 300,
        'page_start': 0,
        'sort': 'recommend',
        'tag': '热门'
    },
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15'
    }
}

"""1.get"""
# response = requests.get(args['url'], params=args['params'], headers=args['headers'])
"""2.post"""
response = requests.post(args['url'], data=args['params'], headers=args['headers'])

movie_data = response.json()['subjects']
save_dir = 'download'
file_name = 'movie.json'
os.makedirs(save_dir, exist_ok=True)
save_file = os.path.join(save_dir, file_name)
with open(save_file, 'w') as f:
    json.dump(movie_data, f)
for moviei in movie_data:
    print("title: {} ; url: {}".format(moviei['title'], moviei['url']))
