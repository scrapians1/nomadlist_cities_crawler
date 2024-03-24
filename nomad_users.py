import scrapy
from scrapy.crawler import CrawlerProcess as Cp
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
class NomadlistCitySpider(scrapy.Spider):
    name = "nlsc"
    custom_settings = {"FEED_FORMAT":"csv",
    "FEED_URI":"nomadlist_users.csv"
    ''}
    start_urls = [f'https://nomadlist.com/assets/autocompleteQueries.json?2_{today}_1']

    def parse(self, response):
        response_json = response.json()
        for item in response_json:
            if item.get('type') == 'user':
                yield item


if __name__ == '__main__':
      proc = Cp(); proc.crawl(NomadlistCitySpider); proc.start()


   