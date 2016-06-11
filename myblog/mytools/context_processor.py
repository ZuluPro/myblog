from mytools.views import TOOLS


def tools(request):
    return {'tools': TOOLS}
