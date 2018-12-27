# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WinterAmzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_item_exp = scrapy.Field()
    product_category = scrapy.Field()
    product_image_url = scrapy.Field()

class DataAsin(scrapy.Item):
    product_data_asin = scrapy.Field()

