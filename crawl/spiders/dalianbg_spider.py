# -*- coding: utf-8 -*-
import scrapy
from crawl.items import CrawlItem
import pymongo

class DalianbgSpider(scrapy.Spider):
    name = "dalianbg"
    allowed_domains = ["dalianbg.com"]
    start_urls = [
        "http://dalianbg.com/",
    ]

    def parse(self, response):
        product_list = response.xpath(".//div[@class='cpfl_con']//li")
        for sel in product_list:
            item = CrawlItem()
            item['title'] = sel.xpath(
                ".//div[@class='divr fr']//p[1]//a//text()").extract()
            item['description'] = sel.xpath(
                ".//div[@class='divr fr']//p[2]/text()").extract()
            yield item
            
            



