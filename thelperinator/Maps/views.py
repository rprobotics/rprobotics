from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .controllers import *
from Activities.productionyelp import *

import copy

# Create your views here.

def map(request):
    counter=0
    lengthList=[]
    context={}
    destinationList = request.session.get('destinationList')
    startingPoint = request.session.get('startingPoint')
    context['req']=destinationList
    #print "printing "
    context['startingPoint'] = startingPoint
    defineShortestPath(startingPoint=startingPoint, destinationList=destinationList, request=request)
    #for y in context['req']:
        #print "firstCity: {0},\tsecondCity: {1},\tdistance{2}".format(y, y['secondCity'],y['distance'])
        #print "\n"
            

    return render(request, "Maps/view_map.html", context)
