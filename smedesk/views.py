import json
from datetime import datetime, timedelta
from typing import Dict

from django.db.models.query import QuerySet
from django.db.transaction import atomic
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from smedesk.api.models import User, Session
from smedesk.email.smedesk_email import SIGNUP_TEMPLATE, send_email
from smedesk.serializers import SignupSerializer, SigninSerializer
from smedesk.settings import SESSION_COOKIE_NAME


# TODO: maybe move custome exceptions to common/utils.py
class ServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Service Unavailable'
    default_code = 'service_unavailable'


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'


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

    with atomic():
        user: User = User.objects.create_user(
            name=name,
            email=email,
            password=password,
            terms=terms
        )

        try:
            send_email(to_email=user.email, template=SIGNUP_TEMPLATE)
        except Exception:
            raise ServiceUnavailable()

    return JsonResponse(
        status=status.HTTP_201_CREATED,
        data={
            'detail': (
                f'Signup was successful, registration email was sent to '
                f'{user.email}'
            ),
        }
    )


@api_view(['POST'])
def signin(request: HttpRequest) -> Response:
    signin_data: Dict = json.loads(request.body)

    serializer: SigninSerializer = SigninSerializer(data=signin_data)
    serializer.is_valid(raise_exception=True)

    email: str = serializer.data.get('email').lower()
    password: str = serializer.data.get('password')

    filtered_user: QuerySet = User.objects.filter(email=email)
    user_exists: bool = filtered_user.exists()

    if not user_exists:
        raise AuthenticationFailed()

    # TODO: maybe find a way to merge filtered_user & user_object
    user_object = User.objects.get(email=email)
    password_matches: bool = user_object.check_password(raw_password=password)

    if not password_matches:
        raise AuthenticationFailed

    # TODO: not sure if the 'objects' warning should be ignored
    session: Session = Session.objects.create(user=user_object)
    response: Response = Response()

    current_time: timezone = timezone.now()
    days_to_expiration: timedelta = timedelta(days=365 * 100)
    expiration_date: datetime = current_time + days_to_expiration

    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        expires=expiration_date,
        value=session.token,
        secure=True,
        httponly=True,
        samesite='Strict'
    )

    return response
