from django_comments.forms import CommentForm as BaseCommentForm
from captcha.fields import ReCaptchaField
from mycomment import moderator


class CommentForm(BaseCommentForm):
    captcha = ReCaptchaField()
