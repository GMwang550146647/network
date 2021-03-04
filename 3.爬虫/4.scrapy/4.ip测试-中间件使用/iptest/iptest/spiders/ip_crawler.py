import scrapy
from ..items import IptestItem


class IpCrawlerSpider(scrapy.Spider):
    name = 'ip_crawler'
    # allowed_domains = ['www']
    start_urls = ['https://gwgp-kk6owjrbujz.i.bdcloudapi.com/aladdin/ip/query']

    def parse(self, response):
        item = IptestItem()
        item['ip'] = response.json().get("ipv4", "IP Error!")
        yield item
