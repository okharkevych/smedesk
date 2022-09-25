from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods

from django.conf import settings


@require_http_methods(['GET'])
def get_sample(r: HttpRequest) -> HttpResponse:
    if settings.ALLOW_POST_NEW_FILES:
        return HttpResponse(status=200, content=b'sample content')
    else:
        return HttpResponse(status=404, content=b'not found')
