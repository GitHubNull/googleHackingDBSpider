# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GooglehackingdbspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    hackStr = scrapy.Field()
    hackStrLink = scrapy.Field()
    Category = scrapy.Field()
    CategoryLink = scrapy.Field()
    pass
