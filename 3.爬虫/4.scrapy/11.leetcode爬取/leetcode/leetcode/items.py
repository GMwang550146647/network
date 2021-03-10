# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LeetcodeItem(scrapy.Item):
    # define the fields for your item here like:
    index = scrapy.Field()
    title = scrapy.Field()
    pass_rate = scrapy.Field()
    difficulty = scrapy.Field()
    desc_url=scrapy.Field()
    desc=scrapy.Field()
