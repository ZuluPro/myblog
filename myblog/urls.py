from django.conf import settings as s
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap

from sitemaps import WebsiteSitemap

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'categories': CategorySitemap,
    'website': WebsiteSitemap,
}

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/weblog/', permanent=True)),
    url(r'^photos$', 'photos.views.photos', name="photos"),
    url(r'^', include('about.urls')),
    url(r'^', include('myapp.urls')),
    url(r'^tools/', include('mytools.urls', namespace='mytools')),
    url(r'^bio/', include('bio.urls')),
    url(r'^bio/', include('bio.items.urls')),
    url(r'^bio/', include('bio.scheduler.urls')),
    url(r'^bio/', include('schedule.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
)

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
)

if s.DEBUG:
    urlpatterns += static(s.STATIC_URL, document_root=s.STATIC_ROOT)
    urlpatterns += static(s.MEDIA_URL, document_root=s.MEDIA_ROOT)
