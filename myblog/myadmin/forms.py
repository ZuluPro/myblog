from django import forms
from zinnia.admin.forms import EntryAdminForm as BaseEntryAdminForm


class EntryAdminForm(BaseEntryAdminForm):
    pingback_enabled = forms.BooleanField(widget=forms.HiddenInput(), initial=0, required=False)
    trackback_enabled = forms.BooleanField(widget=forms.HiddenInput(), initial=0, required=False)
