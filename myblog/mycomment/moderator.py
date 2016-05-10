from django.conf import settings
from akismet import Akismet


def akismet(comment, content_object, request):
    blog_url = request.build_absolute_uri('/')
    akismet = Akismet(key=settings.AKISMET_API_KEY,
                      blog_url=blog_url)

    data = {
        'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
        'user_agent': request.META.get('HTTP_USER_AGENT', ''),
        'referrer': request.META.get('HTTP_REFERER', ''),
        'comment_type': 'comment',
        'comment_author_email': comment.user_email.encode('utf-8'),
        'comment_author_url': comment.user_url.encode('utf-8'),
        'comment_author': comment.user_name,
    }
    return akismet.comment_check(comment.comment.encode('utf-8'),
                                 data=data, build_data=True)
