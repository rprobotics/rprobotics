from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from Activities.models import ActivityType
from Maps.controllers import *
from .forms import *
from .productionyelp import *
from .api import query_api
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
    #print request.session.get('activity') 
    return render(request, "Activities/get_city.html")
   # return HttpResponse("hello activity world")
 
 
 
 
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
    #print "fullList: {0}".format(fullList[6])
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
    import json
    request.session['activity'] = activity
    apikey="AIzaSyASwjacwj6WmBZ5NT3Tq_lGvb9MxizfUsU"
    coords=json.load(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=San+Francisco,+CA&key=AIzaSyASwjacwj6WmBZ5NT3Tq_lGvb9MxizfUsU"))
    baseLoc=coords['results'][0]['geometry']['location']
    longitude=baseLoc['lng']
    latitude=baseLoc['lat']
    
    cityResults=json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=5000&type={2}&key={3}".format(latitude,longitude, activity,apikey)))
    print(cityResults)
    #cityResults = query_api(activity, city)
    #print "cityResults: {0}".format(cityResults)
    context = {"viewCity": cityResults, 'city': city}
    #context = {"viewCity": coords, 'city': city}
    #request.session['cityResults'] = cityResults

    return render(request, "Activities/view_city.html", context)
 
def queryCity(request, city):
    if request.method == "POST":
        form = CityForm(request.POST)
#        print "CityForm: {0}".format(form)
        city_name = request.POST['city'].strip("/")
#        print "city_name: {0}".format(city_name)
        activity = request.POST['activity']
        if form.is_valid():
            return HttpResponseRedirect("{0}/view/{1}".format(city_name, activity))
#            return HttpResponseRedirect(city_name+"/view/"+activity)
    else:
        form = CityForm()
    return render(request, "Activities/get_city.1.html", {'form': form})
