import scrapy
from ..items import IptestItem

class IpCrawlerSpider(scrapy.Spider):
    name = 'ip_crawler'
    # allowed_domains = ['www']
    start_urls = ['https://gwgp-kk6owjrbujz.i.bdcloudapi.com/aladdin/ip/query']

    def parse(self, response):
        item=IptestItem()
        html=response.text
        with open('data/ip.html','w') as f:
            f.write(html)
        ip=response.xpath('//*[@class="ip-container_2lV2g"]').extract_first()
        item['ip']=ip
        yield item


