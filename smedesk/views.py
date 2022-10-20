import json
from typing import Dict

from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.serializers import ValidationError

from smedesk.api.models import User
from smedesk.serializers import SignupSerializer


@api_view(['POST'])
def signup(request: HttpRequest) -> JsonResponse:
    signup_data: Dict = json.loads(request.body)

    serializer: SignupSerializer = SignupSerializer(data=signup_data)
    serializer.is_valid(raise_exception=True)

    name: str = serializer.data.get('name')
    email: str = serializer.data.get('email').lower()
    password: str = serializer.data.get('password')
    terms: bool = serializer.data.get('terms')

    if not terms:
        raise ValidationError(
            {
                "terms": [
                    "You must accept terms and conditions."
                ]
            }
        )

    new_user: QuerySet = User.objects.filter(email=email)
    user_exists: bool = new_user.exists()

    if user_exists:
        raise ValidationError(
            {
                "email": [
                    "This email address is already being used."
                ]
            }
        )

    user: User = User.objects.create_user(
        name=name,
        email=email,
        password=password,
        terms=terms
    )
    # TODO: assign template to const
    signup_template: str = 'd-58f617828d2244979db3a47a1f65dd25'

    return JsonResponse(
        status=201,
        data={
            'detail': 'success'
        }
    )
