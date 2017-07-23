#!/usr/bin/env python

import bz2
import os
import pickle
import json

from bs4 import BeautifulSoup

# some initialization
recipe_dir = os.getcwd() + "/../pickle_recipes"
output_file = open("fixtures/recipes2.json", "w")
json_output_array = []

counter = 1
for recipe in os.listdir(recipe_dir):
    pickle_data = bz2.BZ2File("/{0}/{1}".format(recipe_dir, recipe), 'r')
    try:
        recipe_json = pickle.load(pickle_data)
    except EOFError:
        pass
    
    
    directions = BeautifulSoup(str(recipe_json['directions']), 'html.parser')
    ingredList = BeautifulSoup(str(recipe_json['ingredList']), 'html.parser')


    # Getting rid of the <span></span> that was brought over from the web crawling.
    clean_ingredList = []
    directions_list = []
    for i in ingredList.find_all('span'):
        clean_ingredList.append(i.string)
    for count,i in enumerate(directions.find_all('span')):
        count += 1
        clean_directions = {}
        if i.string != None:
            key = str(count)
            clean_directions['step'] = i.string
            clean_directions['step_num'] = key
            directions_list.append(clean_directions)

    # Create a new json model entry for the recipe to be imported by django
    new_recipe = { 'model': 'core.recipes', 'pk': counter, 'fields': {'ingredList': clean_ingredList, 'directions': directions_list, 'title': str(recipe_json['title'])}}
    
    # add the recipe to json output array
    json_output_array.append(new_recipe)

    
    counter += 1

    # This section can be uncommented to limit number of files tested against, for testing
    """
    if counter == 10:
        json.dump(json_output_array, output_file)        


        exit()    
    """

    pickle_data.close()

json.dump(json_output_array, output_file)
output_file.close()
