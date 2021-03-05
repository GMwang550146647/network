import scrapy

from ..items import WangyiItem
from selenium import webdriver
from config import PROJECT_PATH
import os
import re


class WangyiScrawlerSpider(scrapy.Spider):
    name = 'wangyi_scrawler'
    # allowed_domains = ['https://news.163.com']
    start_urls = ['https://news.163.com/']
    model_urls = []
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    web_driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=os.path.join(PROJECT_PATH, '3.爬虫/2.selenium/driver/chromedriver'))

    def parse(self, response):
        li_list = response.xpath('//*[@id="js_festival_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        model_index = [3, 4, 6, 7, 8]
        for i in model_index:
            li = li_list[i]
            model_url_i = li.xpath('./a/@href').extract_first()
            self.model_urls.append(model_url_i)
            yield scrapy.Request(model_url_i, callback=self.parse_model)

    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')

        for div in div_list:
            item = WangyiItem()
            item['title'] = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item['detail_url'] = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            yield scrapy.Request(item['detail_url'], callback=self.parse_new_detail, meta={'item': item})

    def parse_new_detail(self, response):
        item = response.meta['item']
        text = response.xpath('//*[@id="content"]/div[2]')
        text = text.xpath('./p/text()').extract()
        item['text'] = ' '.join(text)
        return item
