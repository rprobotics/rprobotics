
import scrapy
import pickle
import os
import bz2

from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy import Spider


class RecipeSpider(scrapy.Spider):
    name = 'recipe'
    start_urls = ['http://allrecipes.com/recipe/245119/biscuits-and-gravy-casserole/?internalSource=popular&referringContentType=home%20page&clickId=cardslot%2020', \
    'http://allrecipes.com/recipe/18886/beccas-barbequed-beans/']

    def parse(self, response):
        bsObj = BeautifulSoup(response.body_as_unicode(), "html.parser")
        title = bsObj.find("title").string

        ingredList = bsObj.findAll("span", {"class": "recipe-ingred_txt", \
        "itemprop": "ingredients" })

        directions = bsObj.findAll("span", {"class": "recipe-directions__list--item"})
    
        jsun = {'title': title, 'ingredList': ingredList, 'directions': directions }
        
        pickle_data = bz2.BZ2File('pickle_recipes/{0}.pickle.bz2'.format(title), 'w')        
        pickle.dump(jsun, pickle_data)
        pickle_data.close()
    
    
        for item in response.css('a'):     
            if item.re('similar_recipe_banner'):
                href = item.css('a::attr(href)').extract()[0]
                url = "http://allrecipes.com{0}".format(href)
                yield response.follow(url, self.parse)

