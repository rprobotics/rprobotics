#!/usr/bin/env python

import bz2
import os
import pickle
import json
import re
import random
import units.predefined

from bs4 import BeautifulSoup
from units import unit


# needs logging
# for some reason ounce amounts are being displayed ending with a ), need to fix

# This script is not bug-free yet
# I haven't looked into it yet, but I imagine each ingredient is getting put into DB
# this means there's duplicates stemming from ingredients used in multiple places
# eggs for example may be used in multiple recipes, and will have an entry in ingredients each time
# they're used. The goal is to have one entry in ingredients that's mapped to RecipeIngredient
# which will have the amounts needed for the recipe
def make_recipe():
    # some initialization
    recipe_dir = os.getcwd() + "/../pickle_recipes"
    output_file = open("fixtures/data.json", "w")
    json_output_array = []
    measurements = '(ounces|cup|tablespoon|teaspoon|teaspoons|tablespoons|' \
                   'pound||pounds|ounce|cups|slice|slices|pinch|quart|quarts|divided)'
    counter = 1
    ingred_counter = 0

    for recipe in os.listdir(recipe_dir):
        pickle_data = bz2.BZ2File("/{0}/{1}".format(recipe_dir, recipe), 'r')
        #print('bzip file has been loaded')
        try:
            recipe_json = pickle.load(pickle_data)
        except EOFError:
            pass

        directions = BeautifulSoup(str(recipe_json['directions']), 'html.parser')
        ingredList = BeautifulSoup(str(recipe_json['ingredList']), 'html.parser')


        # Getting rid of the <span></span> that was brought over from the web crawling.
        directions_list = []

        for i in ingredList.find_all('span'):
            #print('in ingredient area')
            # fields dict to hold the actual field values
            # using i_clean, so we can clean up the ingredient strings a bit
            ingredient_fields = {}
            i_clean = i.string
            i_clean = i_clean.split(',')[0]

            # regular expression used retrieve the amount
            #amount = re.compile('^[0-9\/ ]* {0}*'.format(measurements))
            amount = re.compile('^[0-9\/ ]* ([0-9\( ]* (ounce)\)|{0})'.format(measurements))
            #salt_and_pepper = re.compile('^(salt|pepper|black pepper)')
            #print(amount.pattern)
            # regular expression used to retrieve the name of the ingredient
            #name = re.compile('(^(ounce)\) |[a-zA-Z \(\)]*$)')
            name = re.compile('([a-zA-Z ]*$)')
            #name = re.compile('ounce')
            ingredient = re.search(name, i_clean)
            try:
                ingredient = ingredient.group(0).lstrip(' ')
            except:
                pass
            # no numbers in ingred at this point, but measurements are
            # need to remove measurements from the rest of the name
            for j in measurements.split('|'):
                new_j = j.replace('(', '').replace(')', '').replace(' ', '').replace('\n', '')
                if new_j != "":
                    new_j = re.compile('^({0}) '.format(new_j))
                    w = re.search(new_j, ingredient)
                    try:
                        p = len(w.group(0))
                        ingredient = ingredient[p:]
                    except:
                        pass
                    finally:
                        ingredient_fields['name'] = ingredient.replace(')', '')

            try:
                ingredient_fields['amount'] = re.search(amount, i_clean).group(0).strip(' ')
            except:
                pass

            # link recipeingredients to its recipe and ingredients
            ingred_counter += 1
            ingredient_fields['ingredient_id'] = ingred_counter
            ingredient_fields['recipe_id'] = counter

            # create the json format django needs
            ingredient_entry = {'model': 'core.ingredient', 'pk': ingred_counter, 'fields': {'name': ingredient_fields['name']}}
            json_output_array.append(ingredient_entry)

            ingredient_model = {'model': 'core.recipeingredient', 'pk': ingred_counter, 'fields': ingredient_fields}
            json_output_array.append(ingredient_model)


        # Going to create the Recipe model, which is just the directions and title
        for count,i in enumerate(directions.find_all('span')):
            count += 1
            clean_directions = {}
            if i.string != None:
                key = str(count)
                clean_directions['step'] = i.string
                clean_directions['step_num'] = key
                directions_list.append(clean_directions)

        # Create a new json model entry for the recipe to be imported by django
        new_recipe = {'model': 'core.recipe', 'pk': counter,
        'fields': {'directions': directions_list,
        'title': str(recipe_json['title'])}}

        # add the recipe to json output array
        json_output_array.append(new_recipe)

        counter += 1

        # This section can be uncommented to limit number of files tested against, for testing
        if counter == counter_limit:
            json.dump(json_output_array, output_file)
            pickle_data.close()
            return



def make_pantry():
    data_file = json.load(open('fixtures/data.json', 'r'))
    pantry_file = open('fixtures/pantry.json', 'w')
    json_output_array = []

    pantry = {'model': 'core.pantry', 'pk': 1, 'fields': {'owner': 'owner'} }
    json_output_array.append(pantry)

    for counter,i in enumerate(data_file):
        try:
            pantryingredient = {}
            if i['model'] == 'core.recipeingredient':
                ingredient_name = i['fields']['name']
                print('{0}: {1}'.format(i['fields']['amount'], i['fields']['name']))
                pantryingredient['pk'] = counter
                pantryingredient['model'] = 'core.pantryingredient'
                pantryingredient['fields'] = {}
                pantryingredient['fields']['name'] = str(ingredient_name)
                pantryingredient['fields']['ingredient'] = i['pk']
                pantryingredient['fields']['pantry_id'] = 1
                pantryingredient['fields']['amount'] = create_random_amount(ingredient_name)
                json_output_array.append(pantryingredient)
        except:
            pass
    json.dump(json_output_array, pantry_file)
    pantry_file.close()

def create_random_amount(ingredient_name):
    counts = ['eggs', 'garlic', 'carrot', 'celery']
    liquids = ['sauce','ketchup', '']
    weight = ['beef', 'steak', 'sausage', ]
    measure = ['crumbs', 'ketchup', 'onion', 'butter']
    return random.randrange(0,5)

if __name__=='__main__':
    units.predefined.define_units()
    counter_limit = 5
    make_recipe()
    make_pantry()

