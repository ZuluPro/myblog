from django.shortcuts import render
from django.views.generic.base import TemplateView
from zinnia_tinymce.views import StaffMemberRequiredMixin


class PrismFormView(StaffMemberRequiredMixin,
                    TemplateView):
    template_name = 'zinnia_tinymce/prism-form.html'
    content_type = 'text/html'
