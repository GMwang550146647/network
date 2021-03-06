import scrapy

from ..items import PhotoItem


class PhotoCrawlerSpider(scrapy.Spider):
    name = 'photo_crawler'
    # allowed_domains = ['https://sc.chinaz.com/tupian/']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            item = PhotoItem()
            item['img_src'] = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            yield item
