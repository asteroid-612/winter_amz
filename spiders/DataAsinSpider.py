# -*- coding: utf-8 -*-
import scrapy
from winter_amz.items import DataAsin

class DataAsinSpider(scrapy.Spider):
    name = "DataAsins"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1258603011&page=1&bbn=16225018011&ie=UTF8&qid=1545919425&ajr=3",
                  "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1258603011&page=2&bbn=16225018011&ie=UTF8&qid=1545919425&ajr=3"]
    pre_url = "https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1258603011&page="
    post_url = "&bbn=16225018011&ie=UTF8&qid=1545919425&ajr=3"
##    def __init(self):
##        for i in range(1,3): # post number will be the 'last page url + 1'.
##            to_append = DataAsinSpider.pre_url + str(i) + DataAsinSpider.post_url
##            DataAsinSpider.start_url.append(to_append)
##    def start_request(self):
##        for j in range(len(DataAsinSpider.start_url)):
##            yield scrapy.Request(DataAsinSpider.start_url[j], self.parse)
    def parse(self, response):
        items = DataAsin()
        data_asin = response.css('li').xpath('@data-asin').extract()
        items['product_data_asin'] = ",".join(data_asin).strip()
        yield items
