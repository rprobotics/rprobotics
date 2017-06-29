from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404

from search.models import  *
import urllib
import json


#example_list = ['milk', 'butter', 'salt', 'eggs', 'bacon']
example_list = ['chicken','garlic','butter']






def index(request):
    ingredients = ""    
    for count,i in enumerate(example_list):
        if count != len(example_list)-1:
            ingredients += '{0},'.format(i)
        else:
            ingredients += i    
    puppy = urllib.urlopen("http://www.recipepuppy.com/api/?i={0}&q=dinner&p=3".format(ingredients))
    puppy = json.loads(puppy.readlines()[0])['results']
    for i in puppy:
        print i

    print ingredients
    puppy = htmlize(puppy)
    return HttpResponse(puppy)
    
    
    