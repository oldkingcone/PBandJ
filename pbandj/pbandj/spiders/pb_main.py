# -*- coding: utf-8 -*-
import scrapy


class PbMainSpider(scrapy.Spider):
    name = "pb_main"
    allowed_domains = ["pastebin.com"]
    start_urls = (
        'http://www.pastebin.com/',
    )

    def parse(self, response):
        pass
