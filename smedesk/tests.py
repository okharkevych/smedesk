import json
from typing import Dict
from unittest.mock import Mock, patch

import sendgrid
from django.test import TestCase
from requests import HTTPError
from rest_framework.response import Response
from rest_framework.test import APIClient

from smedesk.api.models import User


class TestCommon(TestCase):
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


class TestSignup(TestCommon):

    def setUp(self):
        self.api_client: APIClient = APIClient()

        self.valid_name: str = 'Oleh Kharkevych'
        self.valid_email: str = 'oleg.kharkevich@gmail.com'
        self.valid_password: str = '123456789'

        self.valid_payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.valid_email,
            'terms': True,
            'password': self.valid_password
        }

    def test_invalid_email(self):
        client = self.api_client
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': 'invalidemail',
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
        client = self.api_client
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
        client = self.api_client
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
        client = self.api_client
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
        client = self.api_client
        payload = self.valid_payload

        User.objects.create_user(
            name=self.valid_name,
            email=self.valid_email,
            terms=True,
            password=self.valid_password
        )

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
        client = self.api_client
        payload = self.valid_payload

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
        client = self.api_client
        payload = self.valid_payload

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
