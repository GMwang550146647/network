import scrapy
from ..items import HuyaItem
import os


class HuyaCrawlerSpider(scrapy.Spider):
    name = 'huya_crawler'
    # allowed_domains = ['https://www.huya.com/g/xingxiu']
    start_urls = ['https://www.huya.com/l']
    url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=%d'
    base_url='https://www.huya.com/{}'
    def parse(self, response):
        """
        PS:
            yield scrapy.Request(url=new_url, callback=self.parse_other)
            爬取的时候也可以递归回调自身...如果逻辑是一样的！

        :param response:
        :return:
        """

        li_list = response.xpath('//*[@id="js-live-list"]/li')
        next = response.xpath('//*[@id="laypage_6"]')

        for li in li_list:
            item = HuyaItem()
            item['title'] = li.xpath('./a[2]/text()')[0].extract()
            item['url'] = li.xpath('./a[2]/@href')[0].extract()
            item['likes'] = li.xpath('./span/span[3]/i[2]/text()')[0].extract()
            yield item
        for page in range(2, 186):
            new_url = format(self.url % page)
            yield scrapy.Request(url=new_url, callback=self.parse_other)

    def parse_other(self, response):
        datas = response.json()['data']['datas']
        for data_i in datas:
            item = HuyaItem()
            item['title']=data_i['roomName']
            item['url']=self.base_url.format(data_i['profileRoom'])
            item['likes']=data_i['totalCount']
            yield item
