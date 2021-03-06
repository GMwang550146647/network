import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import MovieItemPart1, MovieItemPart2
from scrapy_redis.spiders import RedisCrawlSpider


class MovieCrawlspiderSpider(RedisCrawlSpider):
    name = 'movie_crawlSpider'
    redis_key = 'fbsQueue'
    # start_urls = ['http://www.4567kan.com/frim/index1.html']
    detail_url = 'http://www.4567kan.com'
    rules = (
        # 页码链接 ->这样格式的网站打开之后应该用这个函数处理(这里只爬取前十页)
        Rule(LinkExtractor(allow=r'/frim/index1.html'), callback='parse_item', follow=True),
        # 详情页
        Rule(LinkExtractor(allow=r'/movie/index43'), callback='parse_detail', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            item = MovieItemPart1()
            desc_url = self.detail_url + li.xpath('./div/a/@href').extract_first()
            item['title'] = li.xpath('./div/a/@title')[0].extract()
            item['desc_url'] = desc_url
            yield item

    def parse_detail(self, response):
        # 接收传参的数据（字典）
        item = MovieItemPart2()
        item['desc_detail'] = response.xpath('//*[contains(@class,"detail-sketch")]/text()').extract_first()
        item['video_url'] = self.detail_url + response.xpath(
            '/html/body/div[1]/div/div/div/div[1]/a/@href').extract_first()
        item['title'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        yield item
