#!/usr/bin/env python


from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://allrecipes.com/recipe/245119/biscuits-and-gravy-casserole/?internalSource=popular&referringContentType=home%20page&clickId=cardslot%2020")
bsObj = BeautifulSoup(html, "html.parser")


similarList = bsObj.findAll("a", {"data-internal-referrer-link": "ml_similar_recipe_banner"})
#similarList = bsObj.findAll("li", {"ng-click": "setAnalyticsCookie('similar recipe')"})



ingredList = bsObj.findAll("span", {"class": "recipe-ingred_txt", \
    "itemprop": "ingredients"
})

directions = bsObj.findAll("span", {"class": "recipe-directions__list--item"})
#directions = bsObj.findAll("li", {"class": "step"})


#for i in similarList:
#    print(i.get('href'))

try:
    print(similarList[0])
except: 
    print(bsObj.prettify())    

#html = urlopen("http://allrecipes.com/recipe/245119/biscuits-and-gravy-casserole/?internalSource=popular&referringContentType=home%20page&clickId=cardslot%2020")
"""
html = urlopen("http://allrecipes.com/{0}".format())
bsObj = BeautifulSoup(html, "html.parser")


similarList = bsObj.findAll("a", {"data-internal-referrer-link": "ml_similar_recipe_banner"})


ingredList = bsObj.findAll("span", {"class": "recipe-ingred_txt", \
    "itemprop": "ingredients"
})

directions = bsObj.findAll("span", {"class": "recipe-directions__list--item"})




"""