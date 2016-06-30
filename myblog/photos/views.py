from django.shortcuts import render
from django.views.decorators.cache import cache_page
from flickr_pony.storage import get_flickr_storage


@cache_page(60*30)
def photos(request):
    storage = get_flickr_storage()
    if storage.user_id:
        photos = storage.list_all_size()
    else:
        photos = []
    return render(request, 'photos.html', {
        'title': "Photo gallery",
        'photos': photos,
    })
