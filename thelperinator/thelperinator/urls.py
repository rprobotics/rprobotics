from django.conf.urls import patterns, include, url
from django.contrib import admin

from Activities import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thelperinator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.map, name='index'),
    url(r'^activity/', include('Activities.urls', namespace='activity')),
    url(r'^maps/', include('Maps.urls', namespace='maps')),
    url(r'^admin/', include(admin.site.urls)),
)
