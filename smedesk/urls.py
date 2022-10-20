from django.urls import path

from smedesk.views import signup

urlpatterns = [
    path('api/signup/', signup),
]
