from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from Activities.models import ActivityType
from Maps.controllers import *
from .forms import *


def views(request):
    return HttpResponseRedirect("/activity/")

def index(request):
    form = StartingPointForm()
    return render(request, "thelperinator/index.html")