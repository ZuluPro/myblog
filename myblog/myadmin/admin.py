from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from zinnia.models import Entry
from zinnia.admin import filters
from zinnia_tinymce.admin import EntryAdminTinyMCE
from myadmin.forms import EntryAdminForm


class EntryAdmin(EntryAdminTinyMCE):
    list_filter = (filters.CategoryListFilter, 'status', 'creation_date',)
    list_display = ('get_title', 'get_categories', 'get_tags',
                    'get_is_visible', 'get_short_url', 'creation_date',
                    'get_image', 'get_comment_count')

    form = EntryAdminForm
    fieldsets = (
        (_('Content'), {
            'fields': (
                ('title', 'status'),
                'lead',
                'content',
                ('image', 'image_caption'),
            )}),
        (_('Publication'), {
            'fields': ('creation_date', 'sites'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Metadatas'), {
            'fields': ('featured', 'excerpt', 'authors', 'related'),
            'classes': ('collapse', 'collapse-closed')}),
        (None, {'fields': (
            'comment_enabled',
            'categories',
            ('tags', 'slug'),
            'pingback_enabled',
            'trackback_enabled',
        )}))

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="%s" height="40px"/>' %
                               obj.image.url)
        return ''
    get_image.short_description = _("Image")

    def get_comment_count(self, obj):
        return obj.comments.count()
    get_comment_count.short_description = _("Comments")


admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdmin)
