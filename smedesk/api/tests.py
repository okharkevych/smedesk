import json
from datetime import timedelta
from typing import Dict
from unittest.mock import Mock, patch

import sendgrid
from django.test import TestCase
from django.utils import timezone
from requests import HTTPError
from rest_framework.response import Response
from rest_framework.test import APIClient

from smedesk.api.models import User, Session
from smedesk.settings import SESSION_COOKIE_NAME


class TestCommon(TestCase):
    valid_name: str = 'Oleh Kharkevych'
    invalid_email: str = 'invalidemail'
    valid_email: str = 'oleg.kharkevich@gmail.com'
    valid_password: str = '123456789'
    signup_payload: Dict = {
        'name': valid_name,
        'email': valid_email,
        'terms': True,
        'password': valid_password
    }

    res_mock: Mock = Mock(
        **{
            'status_code': 202,
            'body': b'mock_body',
            'headers': (
                '''
                Server: nginx
                Date: Wed, 21 Sep 2022 16:00:23 GMT
                Content-Length: 0
                Connection: close
                X-Message-Id: R8uNb8NHSYeena1l6V8x8A
                Access-Control-Allow-Origin: https://sendgrid.api-docs.io
                Access-Control-Allow-Methods: POST
                Access-Control-Allow-Headers: Authorization, Content-Type, On-behalf-of, x-sg-elas-acl
                Access-Control-Max-Age: 600
                X-No-CORS-Reason: https://sendgrid.com/docs/Classroom/Basics/API/cors.html
                Strict-Transport-Security: max-age=600; includeSubDomains
                '''
            )
        }
    )

    mock_send_success: patch = (
        patch.object(
            target=sendgrid.SendGridAPIClient,
            attribute='send',
            side_effect=[res_mock]
        )
    )

    mock_send_error: patch = (
        patch.object(
            target=sendgrid.SendGridAPIClient,
            attribute='send',
            side_effect=HTTPError
        )
    )

    def create_test_user(self) -> User:
        test_user: User = User.objects.create_user(
            name=self.valid_name,
            email=self.valid_email,
            terms=True,
            password=self.valid_password
        )

        return test_user

    def create_test_session(self) -> Session:
        test_user: User = self.create_test_user()
        test_session: Session = Session.objects.create(user=test_user)

        return test_session

    def missing_token_cookie_test(self, endpoint: str):
        client: APIClient = APIClient()

        res: Response = client.post(
            path=f'/api/{endpoint}/',
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Authorization cookie missing."
            }
        )

    def session_does_not_exist_test(self, endpoint: str):
        client: APIClient = APIClient()
        client.cookies[SESSION_COOKIE_NAME] = 'test_cookie_token'

        res: Response = client.post(
            path=f'/api/{endpoint}/',
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Invalid session or inactive user."
            }
        )

    def session_expired_test(self, endpoint: str):
        client: APIClient = APIClient()
        test_user: User = self.create_test_user()
        test_session: Session = Session.objects.create(user=test_user)

        test_session.last_active = timezone.now() - timedelta(days=1000)
        test_session.save()

        client.cookies[SESSION_COOKIE_NAME] = test_session.token

        res: Response = client.post(
            path=f'/api/{endpoint}/',
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Invalid session or inactive user."
            }
        )


class TestSignup(TestCommon):

    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.invalid_email,
            'terms': True,
            'password': self.valid_password
        }
        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                'email': [
                    'Enter a valid email address.'
                ]
            }
        )

    def test_password_less_than_min_length(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.valid_email,
            'terms': True,
            'password': '1234567'
        }
        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has at least 8 characters.'
                ]
            }
        )

    def test_password_more_than_max_length(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.valid_email,
            'terms': True,
            'password': '12345678123456781'
        }
        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                'password': [
                    'Ensure this field has no more than 16 characters.'
                ]
            }
        )

    def test_unaccepted_terms_checkbox(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.valid_email,
            'terms': False,
            'password': self.valid_password
        }
        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                'terms': [
                    'You must accept terms and conditions.'
                ]
            }
        )

    def test_email_already_exists(self):
        client: APIClient = APIClient()
        payload = self.signup_payload

        self.create_test_user()

        res: Response = client.post(
            path='/api/signup/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                'email': [
                    'This email address is already being used.'
                ]
            }
        )

    def test_failed_to_send_email(self):
        client: APIClient = APIClient()
        payload = self.signup_payload

        with self.mock_send_error:
            res: Response = client.post(
                path='/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )

        self.assertEqual(
            res.status_code,
            503
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Service Unavailable"
            }
        )

        self.assertEqual(
            User.objects.filter(email=payload.get('email')).exists(),
            False
        )

    def test_successful_signup(self):
        client: APIClient = APIClient()
        payload = self.signup_payload

        with self.mock_send_success:
            res: Response = client.post(
                path='/api/signup/',
                data=json.dumps(payload),
                content_type='application/json'
            )

        self.assertEqual(
            res.status_code,
            201
        )

        self.assertEqual(
            res.json(),
            {
                'detail': (
                    f'Signup was successful, registration email was sent to '
                    f'{self.valid_email}'
                )
            }
        )

        self.assertEqual(
            User.objects.filter(email=payload.get('email')).exists(),
            True
        )


class TestSignin(TestCommon):

    def setUp(self):
        self.signin_payload: Dict[str, str] = {
            'email': self.valid_email,
            'password': self.valid_password
        }

    def test_empty_email_field(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'email': '',
            'password': self.valid_password
        }
        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "email": [
                    "This field may not be blank."
                ]
            }
        )

    def test_invalid_email(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'email': self.invalid_email,
            'password': self.valid_password
        }
        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "email": [
                    "Enter a valid email address."
                ]
            }
        )

    def test_empty_password_field(self):
        client: APIClient = APIClient()
        payload: Dict[str, str] = {
            'email': self.valid_email,
            'password': ''
        }
        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json(),
            {
                "password": [
                    "This field may not be blank."
                ]
            }
        )

    def test_user_does_not_exist(self):
        client: APIClient = APIClient()
        payload = self.signin_payload

        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Incorrect authentication credentials."
            }
        )

    def test_user_exists_wrong_password(self):
        client: APIClient = APIClient()
        payload = self.signin_payload

        User.objects.create_user(
            name=self.valid_name,
            email=self.valid_email,
            terms=True,
            password='123456781'
        )

        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            401
        )

        self.assertEqual(
            res.json(),
            {
                "detail": "Incorrect authentication credentials."
            }
        )

    def test_successful_signin(self):
        client: APIClient = APIClient()
        payload = self.signin_payload

        self.create_test_user()

        res: Response = client.post(
            path='/api/signin/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            res.status_code,
            200
        )

        self.assertIn(
            member=SESSION_COOKIE_NAME,
            container=res.cookies.keys()
        )


class TestSignout(TestCommon):

    def test_missing_token_cookie(self):
        self.missing_token_cookie_test(endpoint='signout')

    def test_session_does_not_exist(self):
        self.session_does_not_exist_test(endpoint='signout')

    def test_session_expired(self):
        self.session_expired_test(endpoint='signout')

    def test_successful_signout(self):
        client: APIClient = APIClient()
        test_session = self.create_test_session()
        client.cookies[SESSION_COOKIE_NAME] = test_session.token

        res: Response = client.post(
            path='/api/signout/',
            content_type='application/json'
        )
        res_cookie: str = res.cookies.get(SESSION_COOKIE_NAME)

        self.assertEqual(
            res.status_code,
            200
        )

        self.assertIn(
            res_cookie.value,
            ''
        )


class TestCurrentUser(TestCommon):

    def test_missing_token_cookie(self):
        self.missing_token_cookie_test(endpoint='current_user')

    def test_session_does_not_exist(self):
        self.session_does_not_exist_test(endpoint='current_user')

    def test_session_expired(self):
        self.session_expired_test(endpoint='current_user')

    def test_get_current_user(self):
        client: APIClient = APIClient()
        test_session = self.create_test_session()
        client.cookies[SESSION_COOKIE_NAME] = test_session.token

        res: Response = client.get(
            path='/api/current_user/',
        )

        self.assertEqual(
            res.status_code,
            200
        )

        self.assertEqual(
            len(res.data),
            2
        )

        self.assertIsNotNone(res.data.get('uid'))

        self.assertIsNotNone(res.data.get('name'))
