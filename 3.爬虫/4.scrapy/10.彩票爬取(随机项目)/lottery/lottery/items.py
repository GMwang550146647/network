# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    date = scrapy.Field()
    red = scrapy.Field()
    sales = scrapy.Field()
    poolmoney = scrapy.Field()
    content = scrapy.Field()
    prizegrades = scrapy.Field()

