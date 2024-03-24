import scrapy
from scrapy.crawler import CrawlerProcess as Cp
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
class NomadlistCityDetailsSpider(scrapy.Spider):
    name = "nlscd"
    custom_settings = {"FEED_FORMAT":"csv",
    "FEED_URI":"nomadlist_city_details.csv"
    ''}
    start_urls = [f'https://nomadlist.com/static/filter/filter-75a548796990ad9855aa94f08c6b4258.json']

    def parse(self, response):
        response_json = response.json()
        cities = response_json.get('cities')
        for city in cities:
            yield city

if __name__ == '__main__':
      proc = Cp(); proc.crawl(NomadlistCityDetailsSpider); proc.start()


   