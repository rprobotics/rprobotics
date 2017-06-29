from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404



def index(request):
    return HttpResponse("Hello World")