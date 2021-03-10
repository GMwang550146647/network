from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # 使用pipeline
    execute(['scrapy', 'crawl', 'ip_crawler'])
    # 使用文件output
    # execute(['scrapy','crawl','huya_crawler','-o','file_record.csv'])
