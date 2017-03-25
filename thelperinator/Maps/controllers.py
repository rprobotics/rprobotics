#!/usr/bin/env python

# controllers for MVC/API
# This file is far from completed. It is still in a POC stage. 

import sys
import copy
import json
import time
from api import *

from urllib2 import *


def getFirstStep(startingPoint=None, destinationList=None, request=None):
    startHere = {}
    for i in request.session['destinationList']:
       # print i
        if startingPoint == i['firstName']:
#            print i
            if not startHere:
                startHere['startName'] = i['firstName']
                startHere['startValue'] = i['distance']['value']
                startHere['finishName'] = i['secondName']
            else:
                if i['distance']['value'] <= startHere['startValue']:
                    startHere['startName'] = i['firstName']  
                    startHere['startValue'] = i['distance']['value']
                    startHere['finishName'] = i['secondName']
    #print "startHere: {0}".format(startHere)
    return startHere
    
    
def defineShortestPath(startingPoint=None, destinationList=None, request=None):
    print "startingPoint: {0}".format(startingPoint)
    firstStep=getFirstStep(startingPoint, destinationList, request)
    print "firstStep: {0}".format(firstStep)
    theList=[]
    theList.append(firstStep)
    counter=0
    print "Second first step: {0}".format(getFirstStep(firstStep['finishName'], destinationList, request))
    
#    for entry in theList:
#        print entry
"""    
    for destination in destinationList:

        theList.append(getDestination(startingPoint, destinationList, request))
        counter +=1
        
    for entry in theList:
        print entry
"""        
        
    
    
    
    
#    for i in request.session.keys():
#        print request.session[i]
#        print request.session['destinationList']
#        print "\n"
#    print "startingPoint: {0}".format(startingPoint)
    #print "destinationList: {0}".format(destinationList)
    #print "Length of destinationList: {0}".format(len(destinationList))
#     counter=0
#     distanceFromPointList=[]
#     for line in destinationList:
# #        print line
#         if line['firstName'] == startingPoint or line['secondName'] == startingPoint:
#             counter +=1
#             distanceFromPointList.append(line['distance']['value'])
#    print min(distanceFromPointList)
#    print "Length of counter: {0}".format(counter)
    
    
def cleanString(spacedString):
    return spacedString.replace(" ","+")


def setDestinations(destlist, request):
    distanceList=[]
    foobar = destlist
    destlist=[]
    counter=0
    selectedList = request.session.get('selectedList')

    while counter < len(foobar):
#        print "selectedList[{0}]['name']: {1}".format(counter, selectedList[counter]['name'])
#        for name in selectedList['name']:
        dic=foobar[counter]['location']

        state=dic['state_code']
        street=cleanString(dic['address'][0])
        city=cleanString(dic['city'])
        destlist.insert(counter,{'city':city, 'street':street, 'state':state, 'name': selectedList[counter]['name']})
        counter+=1
    dunno=(getDistances(destlist, distanceList))
    print "dunno: {0}".format(dunno)
    counter=0
    for entry in dunno:
        print "counter:\t{0}".format(counter)
        print "getDistance return value:\t{0}".format(getDistance(dunno,counter))
        counter+=1
#    return dunno

def getDistances(destlist, distanceList):

    ### Improvement:
    ### go back to old-improvement way, but do math correctly this time! ={ =P
    counter = len(destlist) - 1
#    print len(destlist)
    while counter > 0:
        cleanDict = {}
        firstCity=destlist[counter]['city']
        firstStreet=destlist[counter]['street']
        firstState=destlist[counter]['state']
        firstName=destlist[counter]['name']
        secondCity=destlist[0]['city']
        secondState=destlist[0]['state']
        secondStreet=destlist[0]['street']
        secondName=destlist[0]['name']
        key="MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDZcoilJSunkG34vKWnUDvQNglR5KN7zcA+k0rnV3LV0APvCuwgZnelIOZ/PJxuFHaK0vB9Biy6msEzl+/QhTGLDEa3zoaImP2o6hTbafu6frc4BcCDtERXodQYrwjxaIF8K//rE4F/EuYvwESMSSxmv77vcNe8JI/xRX20PUBjLp4k7enqbEilYwscUqqldViVLxXnyF3s+w6CxvaI7qK1jcZNH77YdM9jdaSzlnmgIPpBkiKFnvE++IWAYOWzSoQDcUb7lAY94ZaMCqaqLuqDY5ymHHwY2OJNNOEh7koCRnpmVORmf3P7JGBbwLSnLA9LjwDItcwjG3/xLi8iTZm1AgMBAAECggEBAJwjfPEwvqcEs6K/OyfoGfsJQin2xll4xYlpVIjHp2LWimyUaDdfvJvrAvfsOttkgDZw/1SXIXkg9Igqmn4dlhSlTQZhGwNs7//hjfZ7pNEmekOVBcbMo6JVRqouzXojM49JPOu8xujLVlSFd/NP+70QBHeEjLTBgEacQoYw0VIlbMBNdDCc06BzNR8wBagza6eV7aVnfmW4y5mgFLEf+ybGqfmbCUlEZeMt93U5p5Z/JT+ahpuDusKyS36i3H9cw8Wgj7W4XyJdSskJ/xOLE4ViA1HWoeGZtjbVm9LV/FHksxXF4zJQczzcERU01j72peP6s32qAGhmI8f6riojjcUCgYEA/AhR0vWRG7cPUjMxPJXdRqlFDvUAPkHSuWHD6kdGaVBl4TSijqeGvsph0wPIRJEzdVvg2wm/9T/sEZQowYoTXvlRmtCefVBnY3m7GtOAHO3DGKf8AN5BeYbdQpUsgRTuCEiCKTEMbQua1JrGIPGy5QHE523420+FLqFnJRbUrbsCgYEA3N7Wb6vZ/mVYBEu2jpMPxEQLSpZW4tv8Wp78vFu+XQilAUHIqcG3eq9vwFOkCDifCxpXg1LMH1kwVXm9CgrdRSIfg0/hO9E/OU8znH+SVHHL4RlHMDc572O4ykS+WfUoPgKCWa4DF1BURcL1m5p24ZW+omsOKMN+JDEZVDsVp08CgYBinDa3ndFa0LMz7Ee1dsWPIiedBItF0KdMVU48WgrYpdZW2StJOY7lE3ZXA8HV4iIKJxrBWP08TfhloFyZ7RZLMK2XL0zzpwPszfJBOsODjhupiAB3rn5buELWDFvPXYsMvqH+z+wWtlWsHaqrtSXTqG+MRWD7Hg/0AL7EqjwohQKBgQCjOwSbTxQyUE92DUaDo+e5EtiNbQIVcqLTjkAWLG9JbkQT47wayRGCV/ls1+OYN9BCcltOsHguismPwgKVU2Yn24oSj4xTmtbw0bnA5P8N7XPRjc7wsT/dzYMZ6SgMb4QoH86Z3GJobnN5gxXkw4ksOnDCs/+o3KFyud6QQ4JDPQKBgD9gYmhSqCkYlTSKk8JOfddZJInycnsDwOS+ocDtxv5lQZ5KEM0fYWYnVw33P34qSvhrAnVx/0WLtu3iYcHiw4Yvm+G9TD1Ax09GdrHwwfcvGGDJ1z9yYXy4KlvpkalvS2iZhz1qkvKCuaj3Ct2eB04GFMB6xwR+Vv3wQ8yIx5da"
#        key="AIzaSyAIj6k0K_GpKxPH7IHFRGXK5BwDpO1anJA"
#        key="AIzaSyAgiQ2FDTJZFd1bNaVSBqBzJwywxuENkaw"
#        BASE_URL= "https://maps.googleapis.com/maps/api/directions/json?origin={0},+{1},+{2}&destination={3},+{4},+{5}&mode=driving&key={6}"\
#        .format(firstStreet,firstCity,firstState,secondStreet,secondCity,secondState, key)
        BASE_URL= "https://maps.googleapis.com/maps/api/directions/json?origin={0},+{1},+{2}&destination={3},+{4},+{5}&mode=driving"\
        .format(firstStreet,firstCity,firstState,secondStreet,secondCity,secondState)
#        print "Base URL: {0}".format(BASE_URL)
        request = Request(BASE_URL)
        time.sleep(1)
        print "QUERYING GOOGLE! =)"
        response = urlopen(request)
        js = json.loads(response.read())
        cleanDict['firstCity'] = firstCity
        cleanDict['firstState'] = firstState
        cleanDict['firstStreet'] = firstStreet
        cleanDict['firstName'] = firstName
        cleanDict['secondState']=secondState
        cleanDict['secondCity']=secondCity
        cleanDict['secondStreet']=secondState
        cleanDict['secondName'] = secondName
#        print "JSON OUTPUT FROM GOOGLE:\n\t {0}".format(js)
        cleanDict['distance']=js['routes'][0]['legs'][0]['duration']
        distanceList.append(cleanDict)
        #print len(distanceList)
        counter -= 1
    if len(destlist) != 2:
        del destlist[0]
        return getDistances(destlist, distanceList)
    else:
        return distanceList


inp=[
     {'city':'san+francisco', 'state':'CA','street':'100+spear+st'},
     {'city':'san+francisco', 'state':'CA','street':'1+embarcadero'},
     {'city':'el+cerrito', 'state':'CA','street':'11565+San+Pablo+Ave'},
     {'city':cleanString('Santa Rosa'), 'state':'CA','street':cleanString('2525 Gardner Ave')},
     {'city':cleanString('Santa Rosa'), 'state':'CA','street':cleanString('1670 Mendocino Ave')},
     {'city':cleanString('Reno'), 'state':'NV','street':cleanString('1855 E Peckham')},
     {'city':cleanString('Somerville'), 'state':'MA','street':cleanString('180 Somerville Ave')},
 ]


if __name__ == '__main__':
    distanceList = []
    getDistances(inp, distanceList)
    