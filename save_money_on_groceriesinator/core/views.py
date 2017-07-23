from django.shortcuts import render
from django.http import HttpResponse

from core.models import Recipes

def detail(request, recipe_id):
    return HttpResponse("You're looking at recipe %s." % recipe_id)

def results(request, recipe_id):
    response = "You're looking at the results of recipe %s."
    return HttpResponse(response % recipe_id)

def vote(request, recipe_id):
    return HttpResponse("You're voting on recipe %s." % recipe_id)


def index(request):

    #"Classic Spicy Meatloaf Recipe - Allrecipes.com
    latest_recipe_list = Recipes.objects.order_by('title')[:5]
    return HttpResponse(output)
    return HttpResponse('hi')    
