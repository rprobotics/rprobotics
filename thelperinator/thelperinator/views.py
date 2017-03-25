from django.shortcuts import render
from django.http import HttpResponse

import urllib
import urllib2
import json



def views(request):
    return "hello world"
#def index(request):

"""
street="100+osage+drive"
city="salinas"
state="ca"
BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json?origin=1+embarcadero,+san+francisco,+CA&destination={0},+{1},+{2}&mode=driving'.format(street, city, state)
myfile = urllib2.Request(BASE_URL)
local_file = urllib2.urlopen(myfile)
jsun = json.loads(local_file.read())
# Create your views here.
def index(request):
#    print local_file.read()
    context = jsun['routes'][0]
    return render(request, "view_directions.html", context)
"""