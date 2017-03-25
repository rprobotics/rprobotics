#!/usr/bin/env python



#################################################
## TODO 
#################################################
# Create a data structure that contains, at minimum, the length of time for the shortest path, 
# and each beginning:end pair in that path
# Each destination should be put into a list with the first entry being the starting point, 
# the second entry the second step, etc

# A complete data structure is necessary!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#^^^^^^^^^^ IMPORTANT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#################################################


# DATA STRUCTURE:
# INPUT : AN ARRAY CONTAINING ALL THE DESTINATIONS SELECTED
# 

import sys
import copy
import json
import time

from urllib2 import *


def cleanString(spacedString):
    return spacedString.replace(" ","+")

def doSomething(dest1, dest2, lengthCounter, lengthList):
    time.sleep(1)
#    BASE_URL= "https://maps.googleapis.com/maps/api/directions/json?origin={0},+{1},+{2}&destination={3},+{4},+{5}&mode=walking".format(firstStreet,firstCity,firstState,secondStreet,secondCity,secondState)
    BASE_URL= "https://maps.googleapis.com/maps/api/directions/json?origin={0},+{1},+{2}&destination={3},+{4},+{5}&mode=driving".format(firstStreet,firstCity,firstState,secondStreet,secondCity,secondState)    
    request = Request(BASE_URL)
    response = urlopen(request)
    js = json.loads(response.read())
    for i in js['routes']:
        lengthCounter += i['legs'][0]['duration']['value']
    #print "Routes"
    #print js
    #print js['routes']
    #print js['routes'][0]['legs'][0]['duration']
    print js['routes'][0]['legs'][0]['duration']
#    print "lengthCounter:"
#    print lengthCounter
    return lengthCounter

def getDistances(anotherList, data):
    #print anotherList
    counter =1
    while counter <len(anotherList):
        distanceDict={}
        newdistance=anotherList[0]['distance'] - anotherList[counter]['distance']
#        newdistance=anotherList[0]['distance']['value']-5
        distanceDict['distance'] = newdistance
        distanceDict['startStreet'] = anotherList[0]['street']
        distanceDict['startCity'] = anotherList[0]['city']
        distanceDict['startState'] = anotherList[0]['state']
        distanceDict['endStreet'] = anotherList[counter]['street']
        distanceDict['endCity'] = anotherList[counter]['city']
        distanceDict['endState'] = anotherList[counter]['state']
        data.append(distanceDict)
        counter+=1
    if len(anotherList) > 2:
        anotherList.pop(0)
        getDistances(anotherList, data)
    else:
        for i in data:
            i['distance'] = abs(i['distance'])
            #print "Start: {0}, {3} \t End: {1}, {4} \t Distance: {2}".format(i['startStreet'], i['endStreet'], i['distance'],i['startState'], i['endState'])
            #pass
#        print data

def scramble(distancelist, data):
    scrambleCounter=0
    counter = 0
    distanceDict={}
    anotherList=[]
    counterone=0
    countertwo=0
#    print distancelist
#    while counteron < len(

    for r in distancelist:
        for l in data:
            distanceDict={'state':'','street':'','distance':'','city':''}
            if r['street'] == l['endStreet']:
                distanceDict['street'] = l['endStreet']
                distanceDict['state'] = l['endState']
                distanceDict['city'] = l['endCity']
                distanceDict['distance'] = l['distance']
                anotherList.append(distanceDict)
    getDistances(anotherList, data)
#    print data
    

            
def getShortestPath(destlist):
    print destlist
    print "\n"
    print "Starting getShortestPath"
    counter=1
    distanceList
    file=open("output","w")
    file.close()

    while counter < len(destlist):
        firstCity=destlist[0]['city']
        firstStreet=destlist[0]['street']
        firstState=destlist[0]['state']
        secondCity=destlist[counter]['city']
        secondState=destlist[counter]['state']
        secondStreet=destlist[counter]['street']

        BASE_URL= "https://maps.googleapis.com/maps/api/directions/json?origin={0},+{1},+{2}&destination={3},+{4},+{5}&mode=driving".format(firstStreet,firstCity,firstState,secondStreet,secondCity,secondState)    
#        print BASE_URL
        request = Request(BASE_URL)
        response = urlopen(request)
        js = json.loads(response.read())
        distance=js['routes'][0]['legs'][0]['duration']['value']
#        distance=js['routes'][0]['legs'][0]['duration']
#        print js['routes'][0]['legs'][0]['duration']
        data={ 'startCity':firstCity, 'startState':firstState,'startStreet':firstStreet, 'endCity':secondCity,'endState':secondState, 'endStreet':secondStreet, 'distance': distance}
        file=open("output", "a")
        file.write(str(data))
        file.write("\n")
        file.close()
        distanceList.append(data)
        counter+=1
    #print distanceList
    return distanceList


inp=[
         {'city':cleanString('Santa Rosa'), 'state':'CA','street':cleanString('2525 Gardner Ave')},
    {'city':'san+francisco', 'state':'CA','street':'100+spear+st'},
     {'city':'san+francisco', 'state':'CA','street':'1+embarcadero'},
     {'city':'el+cerrito', 'state':'CA','street':'11565+San+Pablo+Ave'},
#     {'city':cleanString('Santa Rosa'), 'state':'CA','street':cleanString('2525 Gardner Ave')},
     {'city':cleanString('Santa Rosa'), 'state':'CA','street':cleanString('1670 Mendocino Ave')},
     {'city':cleanString('Reno'), 'state':'NV','street':cleanString('1855 E Peckham')},
     {'city':cleanString('Somerville'), 'state':'MA','street':cleanString('180 Somerville Ave')},
     
 ]


if __name__ == '__main__':
    distanceList=[]
    distanceList = getShortestPath(inp)
    scramble(inp, distanceList)



