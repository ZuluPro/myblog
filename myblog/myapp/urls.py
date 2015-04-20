from django.conf.urls import patterns, include, url
from myapp import views

urlpatterns = patterns('',
    url(r'^zinnia_tinymce/prism-form.html$', views.PrismFormView.as_view(), name="tinymce-prism-form")
)
