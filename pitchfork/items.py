# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PitchforkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewItem(scrapy.Item):
    artist = scrapy.Field()
    album = scrapy.Field()
    date = scrapy.Field()
    score = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
