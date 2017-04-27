from django.conf.urls import include, url
from django.contrib import admin

from Maps import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'thelperinator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.map, name='index'),
]
