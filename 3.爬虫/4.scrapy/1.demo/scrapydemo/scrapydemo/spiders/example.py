
import scrapy
from ..items import ScrapydemoItem


class ExampleSpider(scrapy.Spider):
    # 爬虫文件的唯一标识
    name = 'example'
    # 允许的域名
    # allowed_domains = ['example.com']
    # 起始的url列表：列表元素会被自动进行请求发送
    start_urls = ['https://dig.chouti.com']

    # 解析数据
    def parse(self, response):
        div_list = response.xpath('//div[contains(@class,"link-item")]')
        for div in div_list:
            # 产生的是Selector对象，我们解析获取的数据就是在对象中
            content = div.xpath('./div/div/div[1]/a/text()')[0].extract()
            item = ScrapydemoItem()
            # 复制给Item ScrapydemoItem.content中
            item['content'] = content
            #返回该对象给管道 (管道接收Spider.parse)
            yield item
