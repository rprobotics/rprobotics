from django.conf.urls import  include, url
from django.contrib import admin
#from django.conf.urls.defaults import *
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'thelperinator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^activity/', include('Activities.urls', namespace='activity')),
    url(r'^maps/', include('Maps.urls', namespace='maps')),
    url(r'^admin/', include(admin.site.urls))
]



"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thelperinator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^activity/', include('Activities.urls', namespace='activity')),
    url(r'^maps/', include('Maps.urls', namespace='maps')),
    url(r'^admin/', include(admin.site.urls)),
)
"""