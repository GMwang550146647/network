from scrapy.cmdline import execute
import os
import sys
if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    #使用pipeline
    execute(['scrapy','crawl','example'])
    #使用文件output
    # execute(['scrapy','crawl','example','-o','file_record.csv'])