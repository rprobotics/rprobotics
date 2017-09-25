from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from core.models import *
from django.shortcuts import get_object_or_404, render


import re
import ast
from random import randrange






def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredList = RecipeIngredient.objects.filter(recipe=recipe_id)

    directions = ast.literal_eval(recipe.directions)

    context = {
        'directions': directions,
        'ingredList': ingredList,
        'title': recipe.title,
        'recipe': recipe
    }
    return render(request, 'recipes/detail.html.j2', context)






def results(request, recipe_id):
    response = "You're looking at the results of recipe %s."
    return HttpResponse(response % recipe_id)

def vote(request, recipe_id):
    return HttpResponse("You're voting on recipe %s." % recipe_id)


def index(request):
    latest_recipe_list = Recipe.objects.order_by('title')#[:5]
    template = loader.get_template('recipes/index.html')    
    context = {
        'latest_recipe_list': latest_recipe_list,
        
    }
    return HttpResponse(template.render(context, request))

def pantry(request):
    ingredient = Ingredient.objects.all()
    pantry = Pantry.objects.all()
    pantryingredient = PantryIngredient.objects.all()

    context = {'ingred': ingredient, 'pantry': pantry, 'pantryingredient': pantryingredient}

    print(len(pantryingredient))

    return render(request, 'recipes/pantry.html.j2', context)

#def find(request):






