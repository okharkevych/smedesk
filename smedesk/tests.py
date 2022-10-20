import json
from typing import Dict

from django.test import TestCase
from rest_framework.response import Response
from rest_framework.test import APIClient

from smedesk.api.models import User


class TestSignup(TestCase):

    def setUp(self):
        self.valid_name = 'Oleh Kharkevych'
        self.valid_email = 'oleg.kharkevich@gmail.com'
        self.valid_password = '123456789'

    def test_invalid_email(self):
        client: APIClient = APIClient()
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
        payload: Dict[str, str] = {
            'name': self.valid_name,
            'email': self.valid_email,
            'terms': True,
            'password': self.valid_password
        }

        User.objects.create_user(
            email=self.valid_email,
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
