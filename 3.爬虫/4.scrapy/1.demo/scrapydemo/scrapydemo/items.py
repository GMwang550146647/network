# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()  # Field -> 万能数据类型
    # def __setattr__(self, key, value):
    #     pass
    # def __getattr__(self, item):
    #     pass
    # def __setitem__(self, key, value):
    #     pass
    # def __getitem__(self, item):
    #     pass
