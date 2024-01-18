# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DANGDANG(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    now_price = scrapy.Field()
    short_title = scrapy.Field()
    pre_price = scrapy.Field()
