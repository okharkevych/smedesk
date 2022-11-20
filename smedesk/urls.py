from typing import List, Dict

import debug_toolbar
from django.conf import settings
from django.urls import path, include
from rest_framework_nested.routers import SimpleRouter

from smedesk.api.views import signup, signin, signout, CurrentUserViewSet

viewsets: List[Dict] = [
    {
        'prefix': r'api/current_user',
        'viewset': CurrentUserViewSet,
        'basename': 'current_user',
    },
]

router = SimpleRouter()

for viewset in viewsets:
    router.register(
        prefix=viewset['prefix'],
        viewset=viewset['viewset'],
        basename=viewset['basename']
    )

urlpatterns = [
    path('api/signup/', signup),
    path('api/signin/', signin),
    path('api/signout/', signout),
]

if settings.DEBUG:
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )

urlpatterns = urlpatterns + router.urls
