# -*- coding: utf-8 -*-
import scrapy
import json 
from winter_amz.items import WinterAmzItem

with open('dataasins.json') as data_file:
    data = json.load(data_file)

class AmazonProductsSpider(scrapy.Spider):
    name = "AmazonItems"
    allowed_domains = ["amazon.com"]
    data_asins = [] # product code list
    for i in range(len(data)):
        data_asins.extend(data[i]["product_data_asin"].split(","))
    for j in range(len(data_asins)):
        data_asins[j] = 'https://www.amazon.com/dp/' + data_asins[j]
    # want to do : start_urls from amazon.com, can't we just extract it from that url?
    # start_urls is initialized in empty form, and the process gets the item code "XXXXXXXXXX"(10digits) from amazon.com

    def start_requests(self):
        for i in range(len(AmazonProductsSpider.data_asins)):
            yield scrapy.Request(AmazonProductsSpider.data_asins[i], self.parse)

    def parse(self, response):
        items = WinterAmzItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        item_exp = response.xpath('//div[@id="feature-bullets"]//li/span[@class="a-list-item"]/text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        image = response.xpath('//img[@id="landingImage"]/@src').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_item_exp'] = ",".join(map(lambda x: x.strip(), item_exp)).strip()
        items['product_category'] = ",".join(map(lambda x: x.strip(), category)).strip()
        items['product_image_url'] = ''.join(image).strip()
        yield items


