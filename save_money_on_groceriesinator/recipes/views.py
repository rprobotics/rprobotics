from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from core.models import Recipes
from django.shortcuts import get_object_or_404, render

import json

import ast

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    directions = [recipe.directions]

    directions = ast.literal_eval(recipe.directions)



    context = {
        'directions': directions,
        'ingredList': ast.literal_eval(recipe.ingredList),
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
    #"Classic Spicy Meatloaf Recipe - Allrecipes.com

    latest_recipe_list = Recipes.objects.order_by('title')[:5]
    template = loader.get_template('recipes/index.html')    
    context = {
        'latest_recipe_list': latest_recipe_list,
        
    }
    return HttpResponse(template.render(context, request))

#def find(request):






