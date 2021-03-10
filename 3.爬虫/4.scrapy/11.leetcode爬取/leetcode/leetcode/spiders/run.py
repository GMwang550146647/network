from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    os.makedirs('data/problems', exist_ok=True)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # 使用pipeline
    execute(['scrapy', 'crawl', 'leetcode_crawler'])
