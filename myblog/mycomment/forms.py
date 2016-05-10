from django import forms
from django_comments.forms import CommentForm as BaseCommentForm
from captcha.fields import ReCaptchaField


class CommentForm(BaseCommentForm):
    captcha = ReCaptchaField()


class CommentAdminForm(BaseCommentForm):
    site = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    is_public = forms.BooleanField(widget=forms.HiddenInput(), initial=1, required=False)
