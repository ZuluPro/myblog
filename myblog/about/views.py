from django.shortcuts import render
from curriculum.models import Resume
from curriculum.views import export_classic as _export_classic
from curriculum.revealjs.views import get_resume as _get_resume


def aboutme(request):
    return render(request, 'about.html', {
        'title': 'About me',
        'resume': Resume.objects.get(pk=1)
    })


def export_classic(request):
    return _export_classic(request, 1)


def get_resume(request):
    return _get_resume(request, 1)
