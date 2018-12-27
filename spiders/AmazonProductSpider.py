# -*- coding: utf-8 -*-
import scrapy
from winter_amz.items import WinterAmzItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class AmazonProductsSpider(scrapy.Spider):
    name = "AmazonItems"
    allowed_domains = ["amazon.com"]
##    data_asin = []
##    start_urls = []
    # response = HtmlResponse(url='https://www.amazon.com/s/ref=sr_nr_n_3?fst=as%3Aoff&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1258603011&bbn=16225018011&ie=UTF8&qid=1545877822&rnid=1040660&ajr=3')
##    def __init__(self, response):
##        data_asin = response.css('li').xpath('@data-asin').extract()
##        for i in range(len(data_asin)):
##            a = "https://www.amazon.com/dp/" + data_asin[i]
##            print(a)
##            start_urls.append(a)
    start_urls = [
        "https://www.amazon.com/dp/B07BKSR1SG", "https://www.amazon.com/dp/B07JKD2378",
        "https://www.amazon.com/dp/B07K4Z7CGB", "https://www.amazon.com/dp/B07KPVSCDS"
        ]
    # want to do : start_urls from amazon.com, can't we just extract it from that url?
    # start_urls is initialized in empty form, and the process gets the item code "XXXXXXXXXX"(10digits) from amazon.com
    

    def parse(self, response):
##        data_asin = response.css('li').xpath('@data-asin').extract()
##        for i in range(len(data_asin)):
##            a = "https://www.amazon.com/dp/" + data_asin[i]
##            print(a)
##            start_urls.append(a)
        items = WinterAmzItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        item_exp = response.xpath('//div[@id="feature-bullets"]//li/span[@class="a-list-item"]/text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_item_exp'] = ",".join(map(lambda x: x.strip(), item_exp)).strip()
        items['product_category'] = ",".join(map(lambda x: x.strip(), category)).strip()
        yield items
