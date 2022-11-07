import debug_toolbar
from django.conf import settings
from django.urls import path, include

from smedesk.views import signup, signin

urlpatterns = [
    path('api/signup/', signup),
    path('api/signin/', signin),
]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
