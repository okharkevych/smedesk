import base64
import os


def gen_token(byte_length: int) -> str:
    bytes_token: bytes = (
        base64.urlsafe_b64encode(s=os.urandom(byte_length))
    )
    str_token: str = bytes_token.decode()

    return str_token


def gen_session_token() -> str:
    return gen_token(byte_length=64)
