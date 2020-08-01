# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # replace with the start URL
    start_urls = [
        'https://www.amazon.com/gp/browse.html?node=16225014011&ref_=nav_em_0_2_15_2__nav_desktop_sa_intl_sports_and_outdoors'
    ]
    page_number = 1

    def parse(self, response):
        item = AmazontutorialItem()

        if AmazonSpider.page_number == 1:

            product_name = response.css('.s-access-title::text').extract()
            product_seller = response.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
            product_price = response.css('.a-price span::text').extract()
            product_image_link = response.css('.cfMarker::attr(src)').extract()
            AmazonSpider.page_number = AmazonSpider.page_number + 1

        else:

            product_name = response.css('.a-size-base-plus::text').extract()
            product_seller = response.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
            product_price = response.css('.a-price span::text').extract()
            product_image_link = response.css('.s-image::attr(src)').extract()

        item['product_name'] = product_name
        item['product_seller'] = product_seller
        item['product_price'] = product_price
        item['product_image_link'] = product_image_link

        yield item

        # link for the next page in the website
        next_page = 'https://www.amazon.com/s?i=sporting-intl-ship&rh=n%3A%2116225014011&page=' + str(AmazonSpider.page_number) + '&qid=1591802128&ref=lp_16225014011_pg_2'
        if AmazonSpider.page_number < 2:  # replace 3 with the number of pages to be scrapped
            yield response.follow(next_page, callback = self.parse)


