from typing import Dict

import requests


class ProductRequest:

    def __init__(self):
        self.url = "https://amazon-products1.p.rapidapi.com/search"
        self.headers = {
            "X-RapidAPI-Key": (
                "74e80338a2msha477d9f5d8d6e7fp121113jsn2d4946395b37"
            ),
            "X-RapidAPI-Host": "amazon-products1.p.rapidapi.com"
        }
        self.timeout = 20

    def _request(self, method: str, **kwargs) -> requests.Response:
        kwargs.update(
            {"timeout": self.timeout}
        )

        return getattr(requests, method)(**kwargs)

    def get(self, params: Dict) -> requests.Response:
        return self._request(
            method="get",
            url=self.url,
            headers=self.headers,
            params=params
        )
