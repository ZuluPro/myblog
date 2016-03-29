from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class WebsiteSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'aboutme',
            'zinnia:entry_archive_index',
            'zinnia:sitemap',
            'photos',
            'zinnia:sitemap',
        ]

    def location(self, item):
        return reverse(item)
