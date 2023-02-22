# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrautosItem(scrapy.Item):
    car_brand = scrapy.Field()
    car_model = scrapy.Field()
    car_priceUSD = scrapy.Field()
    car_priceCOL = scrapy.Field()
    car_imagelink = scrapy.Field()
    pass
