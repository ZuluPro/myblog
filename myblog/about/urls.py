from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^about$', 'about.views.aboutme', name="aboutme"),
    url(r'^about/pdf/$', 'about.views.export_classic', name="my_resume_pdf"),
    url(r'^about/(?P<resume_id>\d*)/$', 'curriculum.views.export_classic', name="resume_pdf"),
    url(r'^about/slide/$', 'about.views.get_resume', name="my_resume_slide"),
    url(r'^about/slide/(?P<resume_id>\d*)/$', 'curriculum.revealjs.views.get_resume', name="resume_slide"),
)
