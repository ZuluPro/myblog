from django.shortcuts import render
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy as reverse
from django.core.cache import cache
from flickr_pony.storage import get_flickr_storage, FlickrError


def home(request):
    return render(request, 'mytools/home.html', {
        'tools': TOOLS,
    })


class ToolView(View):
    def _get_context(self):
        return {}

    def get_context(self):
        context = {'tool': self}
        context.update(self._get_context())
        return context

    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)

    def get_url(self):
        return reverse('mytools:' + self.name)


class FlickrIdView(ToolView):
    name = 'flickrid'
    verbose_name = 'Flickr ID'
    description = 'Get email from Flickr ID or reverse'
    template_name = 'mytools/flickr.html'

    def _get_id(self, email):
        storage = get_flickr_storage()
        try:
            id_ = storage.get_user_id(email)
            cache_key = 'flickr_id:%s' % email
            cache.set(cache_key, id_, 3600*6)
        except FlickrError as err:
            id_ = 'Error: %s' % str(err)
        return id_

    def get(self, request):
        context = self.get_context()
        if request.GET.get('q'):
            cache_key = 'flickr_id:%s' % request.GET['q']
            context['response'] = cache.get(cache_key) or self._get_id(request.GET['q'])
        context['q'] = request.GET['q']
        return render(request, self.template_name, context)


TOOLS = (
    FlickrIdView,
)
