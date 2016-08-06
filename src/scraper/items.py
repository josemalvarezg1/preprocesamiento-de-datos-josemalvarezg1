# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LaptopItem(scrapy.Item):
    marca = scrapy.Field()
    modelo = scrapy.Field()    
    precio = scrapy.Field()
    precio_nuevo = scrapy.Field()
    precio_viejo = scrapy.Field()