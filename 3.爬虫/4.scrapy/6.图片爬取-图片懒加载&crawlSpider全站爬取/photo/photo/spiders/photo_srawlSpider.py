import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PhotoItem

class PhotoSrawlspiderSpider(CrawlSpider):
    name = 'photo_srawlSpider'

    start_urls = ['https://sc.chinaz.com/tupian/']
    # 链接提取器
    # 作用：根据规则提取url
    links = LinkExtractor(allow=r'sc.chinaz.com/tupian/index')
    rules = (
        Rule(links, callback='parse_item', follow=True),
        # Rule(links, callback='parse_item', follow=False), #-> False 代表不遵循...
    )

    def parse_item(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            item = PhotoItem()
            item['img_src'] = 'https:' + div.xpath('./div/a/img/@src2').extract_first()
            yield item
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
