from django.shortcuts import render
from curriculum.models import Resume


def aboutme(request):
    return render(request, 'about.html', {
        'title': 'About me',
        'resume': Resume.objects.get(pk=1)
    })
