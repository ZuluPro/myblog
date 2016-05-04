from django_comments.forms import CommentForm as BaseCommentForm
from captcha.fields import ReCaptchaField


class CommentForm(BaseCommentForm):
    captcha = ReCaptchaField()
