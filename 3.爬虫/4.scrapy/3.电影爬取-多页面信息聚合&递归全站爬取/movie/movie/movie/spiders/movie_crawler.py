import scrapy
from ..items import MovieItem


class MovieCrawlerSpider(scrapy.Spider):
    name = 'movie_crawler'
    # allowed_domains = ['http://www.4567kan.com/frim/index1.html']
    start_urls = ['http://www.4567kan.com/frim/index1.html']
    url = 'http://www.4567kan.com/frim/index1-{}.html'
    detail_url = 'http://www.4567kan.com'
    page = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = MovieItem()
            desc_url = self.detail_url + li.xpath('./div/a/@href').extract_first()
            item['title'] = li.xpath('./div/a/@title')[0].extract()
            item['desc_url'] = desc_url
            yield scrapy.Request(desc_url, callback=self.parse_detail, meta={'item': item})

        if self.page <= 100:
            new_url = self.url.format(self.page)
            print("new page:{}".format(new_url))
            yield scrapy.Request(new_url, callback=self.parse)
            self.page += 1

    def parse_detail(self, response):
        # 接收传参的数据（字典）
        item = response.meta['item']
        item['desc'] = response.xpath('//*[contains(@class,"detail-sketch")]/text()').extract_first()
        video_url = response.xpath('/html/body/div[1]/div/div/div/div[1]/a/@href').extract_first()
        item['video_url'] = self.detail_url + video_url
        yield item
