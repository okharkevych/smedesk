from typing import Dict, List


class Products:

    def __init__(self, res_data: Dict, amount: int):
        self.data = res_data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data["results"]:
            if len(products) == self.amount:
                break
            else:
                if product["prices"]["current_price"] == -1.0:
                    continue
                else:
                    products.append(
                        {
                            "title": product["title"],
                            "image": product["image"],
                            "full_link": product["full_link"],
                            "current_price": (
                                product["prices"]["current_price"]
                            ),
                            "currency": product["prices"]["currency"]
                        }
                    )

        return products
