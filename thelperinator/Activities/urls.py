from django.conf.urls import include, url


from Activities import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<city>([\w_]*|\d*))/$', views.queryCity, name='query'),
    
    
    url(r'^(?P<city>([\w_ ]*|\d*))/view/$', views.viewCity, name='viewCity'),
    url(r'^/(?P<city>([\w_ ]*|\d*))/view/$', views.viewCity, name='viewCity'),
    url(r'^/(?P<city>([\w_ ]*|\d*))/view/(?P<activity>([A-Za-z_]*))/$', views.viewCity, name='viewCity'),

    
    url(r'^/map/$', views.viewMap, name='viewMap')


]