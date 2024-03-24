import scrapy
from scrapy.crawler import CrawlerProcess as Cp
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
class NomadlistCityDetailsSpider(scrapy.Spider):
    name = "nlscd"
    custom_settings = {"FEED_FORMAT":"json",
    "FEED_URI":"nomadlist_details.json"
    ''}
    start_urls = [f'https://nomadlist.com/static/filter/filter-75a548796990ad9855aa94f08c6b4258.json']

    def parse(self, response):
        yield {"details":response.json()}
        

if __name__ == '__main__':
      proc = Cp(); proc.crawl(NomadlistCityDetailsSpider); proc.start()

