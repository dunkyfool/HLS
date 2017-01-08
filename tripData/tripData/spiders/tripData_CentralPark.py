import scrapy
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
        3. (V) store it as json
        4. (V) continue to next page
        '''
        Item = TripdataItem()
        bubbleList = response.xpath(
            '//div[@id="REVIEWS"]/div/div[contains(@class, "review")]/div[@class="col2of2"]/div[@class="innerBubble"]/div[@class="wrap"]'
        )

        for bubble in bubbleList:
            Item['headline'] = bubble.xpath('div[starts-with(@class, "quote")]/a/span/text()').extract()[0]
            Item['score'] = bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "rate")]/img/@alt').extract()[0]
            Item['comment'] = bubble.xpath('div[@class="entry"]/p/text()').extract()[0]
            Item['date'] = bubble.xpath('div[starts-with(@class, "rating ")]/span[starts-with(@class, "ratingD")]/@title').extract()[0]
            yield Item

        #MaxPages = response.xpath(
        #    '//div[@id="REVIEWS"]/div[@class="deckTools btm test"]/div[@class="unified pagination "]/div[@class="pageNumbers"]/a/text()'
        #).extract()[-1]

        next_page = response.xpath('//div[@class="unified pagination "]/child::*[2][self::a]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            with open('currentURL','wb') as f:
                f.write(url)
            yield scrapy.Request(url, self.parse)
