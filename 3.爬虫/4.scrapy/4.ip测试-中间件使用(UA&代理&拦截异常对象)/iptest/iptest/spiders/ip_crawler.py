import scrapy
from ..items import IptestItem
from selenium import webdriver
from config import PROJECT_PATH
import os

class IpCrawlerSpider(scrapy.Spider):
    name = 'ip_crawler'
    # allowed_domains = ['www']
    start_urls = ['https://apis.baidu.com/store/aladdin/land?cardType=ipSearch']
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    web_driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=os.path.join(PROJECT_PATH, '3.爬虫/2.selenium/driver/chromedriver'))
    def parse(self, response):
        item = IptestItem()
        item['ip'] = response.xpath('//*[@id="app"]/div[2]/div/div/div[3]/div[1]/span[2]/text()').extract_first()
        yield item
