# -*- coding: utf-8 -*-
import scrapy


class BikeautotraderSpider(scrapy.Spider):
    name = 'bikeAutoTrader'
    allowed_domains = ['www.autotrader.co.za']
    start_urls = ['http://www.autotrader.co.za/']

    def parse(self, response):
        pass
