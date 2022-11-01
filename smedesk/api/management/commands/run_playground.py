import base64
import os

from django.core.management import base


class Command(base.BaseCommand):

    @staticmethod
    def gen_token(byte_length: int) -> str:
        bytes_token: bytes = (
            base64.urlsafe_b64encode(s=os.urandom(byte_length))
        )
        str_token: str = bytes_token.decode()

        return str_token

    def gen_session_token(self) -> str:
        return self.gen_token(byte_length=64)

    def handle(self, *args, **options):
        token = self.gen_session_token()

        print(f'token: {token}')
        print(f'token type: {type(token)}')
