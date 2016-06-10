from django.conf.urls import patterns, url
from mytools import views


urlpatterns = patterns(
    'mytools',
    url('^$', views.home, name="home"),
    url('flickr/$', views.FlickrIdView.as_view(), name=views.FlickrIdView.name),
)
