import scrapy
from ..items import CrautosItem

class CrautosSpider(scrapy.Spider):
    name = 'crautos'
    start_urls = ['https://crautos.com/autosusados/'
    ]

    def parse(self, response):
        items= CrautosItem()

        car_brand = response.css('.brandtitle::text').extract()
        car_model = response.css('.modeltitle::text').extract
        car_priceUSD = response.css('.preciodolares::text').extract()
        car_priceCOL = response.css('.precio::text').extract()

        items['car_brand'] = car_brand
        items['car_model'] = car_model
        items['car_priceUSD'] = car_priceUSD
        items['car_priceCOL'] = car_priceCOL

        yield items