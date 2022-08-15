import unittest
from unittest.mock import Mock, patch
from typing import Dict, List
import random

import requests

from products.request import ProductRequest
from products.parse import Products


class MockResponse:

    def __init__(self):
        pass

    @staticmethod
    def get_product(
        current_price: float = 135.0,
        title: str = "2022 Newest ASUS Vivobook Laptop",
        image: str = (
            'https://m.media-amazon.com/images/I/81DJ09oDgRL._AC_UY218_.jpg'
        ),
        full_link: str = 'https://www.amazon.com/dp/B09V1S44WC/?psc=1',
        currency: str = "$"
    ) -> Dict:
        return {
            'asin': 'B09V1S44WC',
            'title': title,
            'image': image,
            'full_link': full_link,
            'prices': {
                'current_price': current_price,
                'previous_price': -1.0,
                'currency': currency
            },
            'reviews': {
                'total_reviews': 0,
                'stars': -1.0
            },
            'prime': True,
            'sponsored': True,
            'amazon_choice': False,
            'out_of_stock': False
        }

    def get_products(self, invalid_products: List) -> Mock:
        mock_response: Mock = Mock()
        mock_response.status_code = 200

        valid_products: List = [
            self.get_product() for _ in range(10)
        ]
        products = invalid_products + valid_products

        random.shuffle(products)

        mock_response.json.return_value = {
            'results': products
        }

        return mock_response

    def get_products_price_minus_one(
        self,
        *args,
        **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(current_price=-1.0) for _ in range(10)
            ]
        )

    def get_products_price_less_than_five(
        self,
        *args,
        **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(current_price=3.0) for _ in range(10)
            ]
        )

    def get_products_invalid_title(
        self,
        *args,
        **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[self.get_product(title="") for _ in range(10)]
        )

    def get_products_invalid_image(
        self,
        *args,
        **kwargs
    ) -> Mock:
        invalid_image_url: List = [
            self.get_product(image="dddfff") for _ in range(5)
        ]
        empty_image_url: List = [self.get_product(image="") for _ in range(5)]

        products = invalid_image_url + empty_image_url

        random.shuffle(products)

        return self.get_products(invalid_products=products)

    def get_products_invalid_link(
        self,
        *args,
        **kwargs
    ) -> Mock:
        invalid_full_link: List = [
            self.get_product(full_link="dddfff") for _ in range(5)
        ]
        empty_full_link: List = [
            self.get_product(full_link="") for _ in range(5)
        ]

        products = invalid_full_link + empty_full_link

        random.shuffle(products)

        return self.get_products(invalid_products=products)

    def get_products_invalid_currency(
        self,
        *args,
        **kwargs
    ) -> Mock:
        return self.get_products(
            invalid_products=[
                self.get_product(currency="€") for _ in range(10)
            ]
        )


class TestProducts(unittest.TestCase):

    def execute_request_and_get_products(self) -> List:
        request = ProductRequest()
        res: requests.Response = request.get(
            params={
                "country": "US",
                "query": "Laptop"
            }
        )
        products = Products(
            res_data=res.json(),
            amount=5
        ).get()

        return products

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_price_minus_one
    )
    # Check whether the price is valid.
    def test_products_price_higher_than_minus_one(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertGreater(product["current_price"], -1.0)

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_price_less_than_five
    )
    # Check whether the price fits our preferences.
    def test_products_price_higher_than_five(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertGreater(product["current_price"], 5.0)

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_invalid_title
    )
    def test_products_has_valid_title(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertNotEqual(product["title"], "")

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_invalid_image
    )
    def test_products_has_valid_image(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertIn(".jpg", product["image"])

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_invalid_link
    )
    def test_products_has_valid_link(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertIn("www.amazon.com", product["full_link"])

    @patch.object(
        requests,
        "get",
        side_effect=MockResponse().get_products_invalid_currency
    )
    def test_products_has_valid_currency(self, *args, **kwargs):
        products: List = self.execute_request_and_get_products()

        for product in products:
            self.assertIn("$", product["currency"])


if __name__ == "__main__":
    unittest.main()
