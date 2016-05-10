from django.contrib import admin
from django.utils.translation import ugettext as _
from django_comments.admin import CommentsAdmin as BaseCommentsAdmin
from django_comments.models import Comment


class CommentsAdmin(BaseCommentsAdmin):
    list_display = ('name', 'content_type', 'get_object_absolute_url', 'ip_address', 'submit_date', 'is_public', 'is_removed')
    list_filter = ('submit_date', 'is_removed')
    readonly_fields = ('content_type', 'object_pk')

    fieldsets = (
        (
            None,
            {'fields': (('content_type', 'object_pk',),)}
        ),
        (
            _('Content'),
            {'fields': (('user', 'user_name', 'user_email', 'user_url'), 'comment')}
        ),
        (
            _('Metadata'),
            {'fields': (('submit_date', 'ip_address', 'is_removed'),)}
        ),
    )

    def get_object_absolute_url(self, obj):
        try:
            url = obj.content_object.get_absolute_url()
            return '<a href="%s">%s</a>' % (url, obj)
        except:
            return ''
    get_object_absolute_url.short_description = _("Object")
    get_object_absolute_url.allow_tags = True

# TODO: WTF
try:
    admin.site.unregister(Comment)
except:
    pass
admin.site.register(Comment, CommentsAdmin)
