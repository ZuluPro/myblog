from django.conf.urls import patterns, url
from mytools import views


urlpatterns = patterns(
    'mytools',
    url('^$', views.home, name="home"),
)
for tool in views.TOOLS:
    tool_url = '%s/$' % tool.name
    urlpatterns += (
        url(tool_url, tool.as_view(), name=tool.name),
    )
