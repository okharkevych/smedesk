from typing import Dict, List


class Products:

    def __init__(self, res_data: Dict, amount: int):
        self.data = res_data
        self.amount = amount

    def get(self) -> List:
        products: List = []

        for product in self.data["results"]:
            invalid_attributes: bool = (
                -1.0 <= product["prices"]["current_price"] < 5.0 or
                product["title"] == "" or
                ".jpg" not in product["image"] or
                "www.amazon.com" not in product["full_link"] or
                "$" not in product["prices"]["currency"]
            )
    
            if len(products) == self.amount:
                break
            else:
                if invalid_attributes:
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
