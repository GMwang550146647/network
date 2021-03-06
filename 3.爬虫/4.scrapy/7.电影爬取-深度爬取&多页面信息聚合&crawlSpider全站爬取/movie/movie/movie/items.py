# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItemPart1(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    desc_url = scrapy.Field()


class MovieItemPart2(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    desc_detail = scrapy.Field()
    video_url = scrapy.Field()
