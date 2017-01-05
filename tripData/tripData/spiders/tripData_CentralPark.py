import scrapy
from scrapy.selector import Selector
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
        1. parse all headline, comment, date, and score
        2. pass it to item
        3. store it as json
        4. continue to next page
        '''
        bubbleList = response.xpath(
            '//div[@id="REVIEWS"]/div/div[contains(@class, "review")]/div[@class="col2of2"]/div[@class="innerBubble"]/div[@class="wrap"]')
        for bubble in bubbleList:
            print bubble.xpath('div[starts-with(@class, "quote")]/a/span/text()').extract()
            print bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "rate")]/img/@alt').extract()
            print bubble.xpath('div[@class="entry"]/p/text()').extract()
            print bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "ratingD")]/@title').extract()
