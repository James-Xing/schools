# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class SchoolsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = Field()
    phone_number = Field()
    email = Field()
    physical_address = Field()
    postal_address = Field()

