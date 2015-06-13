from django.conf import settings as s
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap,
}

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url='/weblog/', permanent=True)),
    url(r'^about$', 'about.views.aboutme', name="aboutme"),
    url(r'^', include('myapp.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/tools/', include('admin_tools.urls')),
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
