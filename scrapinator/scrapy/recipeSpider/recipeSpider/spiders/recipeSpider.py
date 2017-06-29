from scrapy.selector import Selector
from scrapy import Spider
#from recipeSpider.items import Article




class Recipespider(Spider):
    name = "recipe"
    allowed_domains = ["allrecipes.com"]
    start_urls = ["http://allrecipes.com/recipe/245119/biscuits-and-gravy-casserole/?internalSource=popular&referringContentType=home%20page&clickId=cardslot%2020"]
    def start_request(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        print("yes")
    