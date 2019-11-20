# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class ScrapyCaseItem(scrapy.Item):
    title = Field()
    content = Field()
    time = Field()
    web=Field()
