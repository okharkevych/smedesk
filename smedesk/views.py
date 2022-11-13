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
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ViewSet

from smedesk.api.authentication.api import (
    get_authorized_session,
    PrivateAPIAuthentication
)
from smedesk.api.email.smedesk_email import SIGNUP_TEMPLATE, send_email
from smedesk.api.exceptions.custom_exceptions import (
    ServiceUnavailable,
    AuthenticationFailed
)
from smedesk.api.models import User, Session
from smedesk.api.serializers.signin import SigninSerializer
from smedesk.api.serializers.signup import SignupSerializer
from smedesk.api.serializers.user import CurrentUserSerializer
from smedesk.settings import SESSION_COOKIE_NAME, SESSION_DURATION


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

    user_queryset: QuerySet = User.objects.filter(email=email)
    user_exists: bool = user_queryset.exists()

    if not user_exists:
        raise AuthenticationFailed()

    user: User = user_queryset.first()
    password_matches: bool = user.check_password(raw_password=password)

    if not password_matches:
        raise AuthenticationFailed

    session: Session = Session.objects.create(user=user)
    response: Response = Response()

    current_time: timezone = timezone.now()
    time_to_expiration: timedelta = SESSION_DURATION
    expiration_date: datetime = current_time + time_to_expiration

    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        expires=expiration_date,
        value=session.token,
        secure=True,
        httponly=True,
        samesite='Strict'
    )

    return response


@api_view(['POST'])
def signout(request: HttpRequest) -> Response:
    session: Session = get_authorized_session(request=request)

    session.last_active = timezone.now()
    session.is_active = False
    session.save()

    response: Response = Response()
    response.delete_cookie(key=SESSION_COOKIE_NAME)

    return response


class CurrentUserViewSet(ViewSet):
    authentication_classes = [PrivateAPIAuthentication]

    @staticmethod
    def list(request: HttpRequest) -> Response:
        return Response(
            CurrentUserSerializer(instance=request.user).data
        )
