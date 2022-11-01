from django.urls import path

from smedesk.views import signup, signin

urlpatterns = [
    path('api/signup/', signup),
    path('api/signin/', signin),
]
