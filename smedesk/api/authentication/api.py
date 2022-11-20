from typing import Union, Tuple

from django.http.request import HttpRequest
from django.utils import timezone
from rest_framework.authentication import BaseAuthentication

from smedesk.api.exceptions.custom_exceptions import (
    AuthorizationFailed,
    SessionFailed
)
from smedesk.api.models import User, Session
from smedesk.settings import SESSION_COOKIE_NAME, SESSION_DURATION


class NoAuthentication(BaseAuthentication):

    def authenticate(self, request: HttpRequest):
        return None, None

    def authenticate_header(self, request: HttpRequest) -> str:
        return 'Cookie'


def get_authorized_session(request: HttpRequest) -> Session:
    token: Union[str, None] = request.COOKIES.get(SESSION_COOKIE_NAME)

    if not token:
        raise AuthorizationFailed()

    try:
        session: Session = (
            Session
            .objects
            .select_related('user')
            .get(
                is_active=True,
                token=token,
                last_active__gte=timezone.now() - SESSION_DURATION
            ))
    except Session.DoesNotExist:
        raise SessionFailed()

    return session


class PrivateAPIAuthentication(NoAuthentication):

    def authenticate(self, request: HttpRequest) -> Tuple[User, Session]:
        session: Session = get_authorized_session(request=request)

        return session.user, session
