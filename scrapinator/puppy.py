#!/usr/bin/env python


from urllib.request import urlopen
from bs4 import BeautifulSoup

import json
import random
import datetime
import pickle

# will need an api to handle measurements, specifically
# a set of functions to determine form (liquid, solid, weight, etc)
# and to be able to correctly determine how much a person has, a much they need,
# and how much is left over after.


example_list = {}
random.seed(datetime.datetime.now)
pantry_file = open("pantry.txt", "r")
for line in pantry_file:
    line = line.strip("\n")
    example_list[line] = {"quantity": int(random.uniform(1,5))}

print(example_list)
#for value,key in enumerate(example_list):
#for value in example_list:
#    html = urlopen("http://www.recipepuppy.com/api/?i={0}&q=dinner".format(value))
#    puppy = json.loads(html.readlines()[0])['results']
#    example_list[value]['recipe'] = puppy

#pickle_dump = open("pickle_dump", "wb")
#pickle.dump(example_list, pickle_dump)

pickle_dump = open("pickle_dump", "rb")
example_list = pickle.load(pickle_dump)


print(example_list['chicken']['recipe'][0])
#bsObj = BeautifulSoup(html, "html.parser")



#print(puppy)
#print(bsObj)