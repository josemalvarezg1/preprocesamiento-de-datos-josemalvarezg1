# -*- coding: utf-8 -*-
"""
@author: José Manuel Alvarez - CI 25038805
"""

import os
os.getcwd()
#------------------------------MODIFICAR--------------------------------------
os.chdir('/home/jose/Documentos/Tarea1_25038805/src/scraper')
#----------------------------------------------------------------------------

import scrapy
from scrapy.http import Request
from scraper.items import LaptopItem

class PcelSpider(scrapy.Spider):
    name = "pcel"
    allowed_domains = ["pcel.com"]
    start_urls = ('https://pcel.com/computadoras/laptops',)

    def parse(self, response):
        for product in response.xpath('//div[@class="product-list"]/table/tr[position() mod 2 = 1]'):
            laptop = LaptopItem()
            laptop['marca'] = ''.join(product.xpath('.//img[contains(@src, "manufacturer")]/@alt').extract())
            laptop['modelo'] = ''.join(product.xpath('.//div[@class="name"]/a/text()[1]').extract()).strip()
            laptop['precio'] = ''.join(product.xpath('.//div[@class="price"]/text()').re('[0-9.]'))
            laptop['precio_nuevo'] = ''.join(product.xpath('.//div[@class="price-new"]/text()').re('[0-9.]'))
            laptop['precio_viejo'] = ''.join(product.xpath('.//div[@class="price-old"]/text()').re('[0-9.]'))
            yield laptop
        next_url = ''.join(response.xpath('//div[@class="links"]/a[text()=">"]/@href').extract())
        if next_url:
            yield Request(next_url, callback=self.parse)
