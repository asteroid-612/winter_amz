# -*- coding: utf-8 -*-
import scrapy
from winter_amz.items import WinterAmzItem

class AmazonProductsSpider(scrapy.Spider):
    name = "AmazonItems"
    allowed_domains = ["amazon.com"]

    start_urls = [
        "https://www.amazon.com/dp/B07BKSR1SG", "https://www.amazon.com/dp/B07JKD2378",
        "https://www.amazon.com/dp/B07K4Z7CGB", "https://www.amazon.com/dp/B07KPVSCDS"
        ]

    def parse(self, response):
        items = WinterAmzItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        item_exp = response.xpath('//div[@id="feature-bullets"]//li/span[@class="a-list-item"]/text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_item_exp'] = ",".join(map(lambda x: x.strip(), item_exp)).strip()
        items['product_category'] = ",".join(map(lambda x: x.strip(), category)).strip()
        yield items
