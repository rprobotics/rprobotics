from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from Activities.models import ActivityType
from Maps.controllers import *
from .forms import *

from .controllers import *


import urllib
import urllib2
import json

# Create your views here.
    
def map(request):
    return HttpResponseRedirect("/maps")
    firstList = request.session.get('selectedList')[0]['location']
    secondList = request.session.get('selectedList')[1]['location']
    firstStreet=formatDest(firstList['address'][0])
    firstCity=formatDest(firstList['city'])
    firstState=firstList['state_code']
    secondStreet=formatDest(secondList['address'][0])
    secondCity=formatDest(secondList['city'])
    secondState=secondList['state_code']
#    street="311+osage+drive"
#    city = "salinas"
#    state="ca"
    BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json?origin={3},+{4},+{5}&destination={0},+{1},+{2}&mode=driving'.format(secondStreet, secondCity, secondState, firstStreet, firstCity, firstState)
    myfile = urllib2.Request(BASE_URL)
    local_file = urllib2.urlopen(myfile)
    jsun = json.loads(local_file.read())
    context = jsun['routes'][0]['legs'][0]['steps']
    context = {"stuffs": context}
    return render(request, "Activities/view_directions.html", context)





# Create your views here.
def index(request):
    return render(request, "Activities/index.html")
    context = {}    
    if request.method == "POST":
        form = StartingPointForm(request.POST)
        home_loc = request.POST['home_loc'].strip("/")
        if form.is_valid():
            home_loc = request.POST.get('home_loc')
            context['home_loc'] = home_loc      
            request.session['home_loc'] = home_loc
            return render(request, "Activities/get_city.html", context)
    #return HttpResponseRedirect("/")
 
  
def queryCity(request, city):
    if request.method == "POST":
        form = CityForm(request.POST)
        city_name = request.POST['city'].strip("/")
        activity = request.POST['activity']
        if form.is_valid():
            return HttpResponseRedirect("{0}/view/{1}".format(city_name, activity))
    else:
        form = CityForm()
    return render(request, "Activities/get_city.1.html", {'form': form})
 
 
 
def viewMap(request):
    context = {}
    city_name = request.POST.get('city_name')
    test = request.POST.getlist('activityChoice')
    startingPoint = request.POST.get('startingPoint')
#    print "Starting Point: {0}".format(startingPoint)
    request.session['startingPoint'] = startingPoint
    l=0
    selectedList = []
    fullList = request.session.get('cityResults')
    print "fullList: {0}".format(fullList)
    for i in fullList:
        if i['name'] in test or i['name'] == startingPoint:
            selectedList.append(i)
            
#    print "Length of selectedList: {0}".format(len(selectedList))
    context['selectedList'] = selectedList
    request.session['selectedList'] = selectedList
    #This query should be moved back to maps to retain any service-based query integrity to individual services
    # e.g. keep the querying of Google Maps in the maps section
    newStuff = setDestinations(request.session.get('selectedList'), request)
    #print "newstuff: \t {0}".format(newStuff)
    request.session['destinationList']=newStuff
    return HttpResponseRedirect("/")
 
 
 # refactor cityResults to cityActivities; it more accurately describes the results
def viewCity(request, city, activity):
    apikey="AIzaSyASwjacwj6WmBZ5NT3Tq_lGvb9MxizfUsU"
    
    coords=json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=San+Francisco,+CA&key=AIzaSyASwjacwj6WmBZ5NT3Tq_lGvb9MxizfUsU"))
    baseLoc=coords['results'][0]['geometry']['location']
    longitude=baseLoc['lng']
    latitude=baseLoc['lat']
    
    cityResults=json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=5000&type={2}&key={3}".format(latitude,longitude, activity,apikey)))
    
    request.session['activity'] = activity  
    context = {"viewCity": cityResults, 'city': city}
    request.session.put(cityResults)
    print(cityResults)
    return render(request, "Activities/view_city.html", context)

