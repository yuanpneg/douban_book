# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    recruitPostId = scrapy.Field()

    recruitPostName = scrapy.Field()

    countryName = scrapy.Field()

    locationName = scrapy.Field()

    GName = scrapy.Field()

    productName = scrapy.Field()

    categoryName = scrapy.Field()

    responsibility = scrapy.Field()

    lastUpdateTime = scrapy.Field()

    postURL = scrapy.Field()


