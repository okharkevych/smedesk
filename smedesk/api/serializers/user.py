from rest_framework.serializers import ModelSerializer

from smedesk.api.models import User


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'name']
