import scrapy
from scrapy.selector import Selector
from tripData.items import *
from pprint import pprint

class Spider(scrapy.Spider):
    name = 'tripData_CentralPark'
    allowed_domains = ['tripadvisor.com']
    base_url = "http://www.tripadvisor.com"
    start_urls = [
        base_url + '/Attraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html',
    ]


    def parse(self, response):
        '''
        1. (v) parse all headline, comment, date, and score
        2. (v) pass it to item ([WARN] one review per time)
        3. store it as json
        4. continue to next page
        '''
        Item = TripdataItem()
        bubbleList = response.xpath(
            '//div[@id="REVIEWS"]/div/div[contains(@class, "review")]/div[@class="col2of2"]/div[@class="innerBubble"]/div[@class="wrap"]'
        )

        for bubble in bubbleList:
            Item['headline'] = bubble.xpath('div[starts-with(@class, "quote")]/a/span/text()').extract()
            Item['score'] = bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "rate")]/img/@alt').extract()
            Item['comment'] = bubble.xpath('div[@class="entry"]/p/text()').extract()
            Item['date'] = bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "ratingD")]/@title').extract()

        pprint(Item)
