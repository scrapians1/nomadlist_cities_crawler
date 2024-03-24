import scrapy
from scrapy.crawler import CrawlerProcess as Cp

class NomadlistCitySpider(scrapy.Spider):
    name = "nlsc"
    custom_settings = {"FEED_FORMAT":"csv",
    "FEED_URI":"nomadlist_cities.csv"
    ''}
    start_urls = ['https://nomadlist.com/assets/autocompleteQueries.json?2_2024-03-24_1']

    def parse(self, response):
        response_json = response.json()
        for item in response_json:
            if item.get('type') == 'city':
                yield item


   

if __name__ == "__main__":
    proc = Cp(); proc.crawl(NomadlistCitySpider); proc.start()