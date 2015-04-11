from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/', include(admin.site.urls)),
]
