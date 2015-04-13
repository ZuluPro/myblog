from django.conf import settings as s
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if s.DEBUG:
    urlpatterns += static(s.STATIC_URL, document_root=s.STATIC_ROOT)
