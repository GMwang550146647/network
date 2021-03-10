import scrapy
from ..items import LeetcodeItem
from selenium import webdriver
from config import PROJECT_PATH
import os
from redis import Redis

class LeetcodeCrawlerSpider(scrapy.Spider):
    conn = Redis(host='127.0.0.1', port=6379)
    name = 'leetcode_crawler'
    domain = 'https://leetcode-cn.com'
    detail_url_pattern = [r'problems']
    problemset_url_pattern = [ r'problemset']
    start_urls = ['https://leetcode-cn.com/problemset/all/#page-2']
    url_format = 'https://leetcode-cn.com/problemset/all/#page-{}'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    web_driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=os.path.join(PROJECT_PATH, '3.爬虫/2.selenium/driver/chromedriver'))
    page = 2

    def parse(self, response):
        questions_trs = response.xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table//tr')
        for tr_i in questions_trs:
            try:
                item = LeetcodeItem()
                item['desc_url'] = self.domain + tr_i.xpath('./td[3]/span/div/a/@href').extract_first()
                item['title'] = tr_i.xpath('./td[3]/span/div/a/text()').extract_first()
                item['index'] = tr_i.xpath('./td[2]/text()').extract_first()
                item['pass_rate'] = tr_i.xpath('./td[5]/text()').extract_first()
                item['difficulty'] = tr_i.xpath('./td[6]/span/text()').extract_first()
                ex = self.conn.sadd('leetcode_index', item['index'])
                if ex == 1:
                    print("捕获到最新消息: {}.{}".format(item['index'],item['title']))
                    yield item
                else:
                    print("老消息啦 : {}.{}".format(item['index'],item['title']))
                yield scrapy.Request(item['desc_url'], callback=self.parse_details, meta={'item': item})
            except Exception as err:
                print("Error：{}".format(err))

    def parse_details(self, response):
        item = response.meta.get('item')
        text = response.xpath('//*[@id="question-detail-main-tabs"]/div[2]/div/div[2]/div')
        item['desc'] = text[0].xpath('string(.)').extract_first()
        yield item
