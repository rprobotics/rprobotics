from django.shortcuts import render
from django.http import HttpResponse

from forms import *

def views(request):
    return "hello world"

def index(request):
    form = StartingPointForm()
    return render(request, "thelperinator/index.html", {'form': form})