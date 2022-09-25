import requests
from typing import Dict, List


# TODO: Exercise 1: A proper request following all the previous instructions
#  1. Add variable type to the 'response'
#  2. Instead of using separate 'url' variable,
#    move 'https://amazon-products1.p.rapidapi.com/search' in .get(url=...)
#  3. Instead of using separate 'headers' variable,
#    move {... headers_content ...} in .get(headers=...)
#  4. Instead of using separate 'querystring' variable,
#    move {... querystring_content ...} in .get(params=...)
#  5. Choose one either single or double quotes,
#    and stick with them - replace all of them with one type.

###
# Laptop
# PC Screen
# Headphones
# Notepad
# Pen
###

# response: requests.models.Response = requests.get(
#     url="https://amazon-products1.p.rapidapi.com/search",
#     headers={
#         "X-RapidAPI-Key": (
#             "74e80338a2msha477d9f5d8d6e7fp121113jsn2d4946395b37"
#         ),
#         "X-RapidAPI-Host": "amazon-products1.p.rapidapi.com"
#     },
#     params={"country": "US", "query": "Laptop"}
# )
# data: Dict = response.json()
#
# print(f"raw data: {data}\n")
# print(f"number of results: {len(data['results'])}\n")
# print(f"1st result title: {data['results'][0].get('title')}\n")
# print(f"1st result image: {data['results'][0].get('image')}\n")
# print(f"1st result full link: {data['results'][0].get('full_link')}\n")
# print(f"1st result prices: {data['results'][0].get('prices')}\n")

# TODO: Exercise 2: Create a 'ProductRequest' class
#  1. Create a new 'ProductRequest' class blueprint
#  2. Create a new method called 'def _request(self) -> requests.Response:'
#  3. Move the content of 'Exercise 1' to the new '_request' method
#  (return the response)

# TODO: Exercise 3: Move parts that don't change to the __init__
#  1. Create a new 'self.url' variable in '__init__' method
#  (and use it in code)
#  2. Create a new 'self.headers' variable in '__init__' method
#  (and use it in code)

# TODO: Exercise 4: Add 'timeout' (in case we can't reach the API url)
#  1. Create a separate method called '.get()' in 'ProductRequest' class
#  2. Adjust '_request' method to use 'getattr()' and '**kwargs'
#  (see the video)
#  3. Add new variable called 'self.timeout' to __init__ method (see the video)
#  4. Update 'kwargs' with 'self.timeout' in '_request' method (see the video)
#  5. Adjust '.get()' method to use '_request' method (see the video)


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


# TODO: Exercise 5: Data extraction for the first product
#  1. Use 'ProductRequest' to create a new request
#  2. Assign the result of .get() method execution to a new variable
#  called 'res'
#  3. Create a new variable 'res_data: Dict = res.json()'
#  4. Get the first product from the 'results' key in 'res_data'
#    and assign it to a new variable called 'product'
#  5. Find out how to access product fields:
#    'title', 'image', 'full_link', 'current_price', 'currency'
#    using 'product' variable
#  6. Create a new empty 'List' variable called 'products'
#  7. Append a new item
#    (Dict with product 'title', 'image', 'full_link', 'current_price',
#    'currency') to 'products'

data: Dict = {
    "country": "US",
    "query": "Laptop"
}

request = ProductRequest()
res: requests.Response = request.get(params=data)


# res_data: Dict = res.json()


# product: Dict = res_data["results"][0]
#
# title: str = product["title"]
# image: str = product["image"]
# full_link: str = product["full_link"]
# current_price: float = product["prices"]["current_price"]
# currency: str = product["prices"]["currency"]
#
# products: List = []
#
# products.append(
#     {
#         "title": product["title"],
#         "image": product["image"],
#         "full_link": product["full_link"],
#         "current_price": product["prices"]["current_price"],
#         "currency": product["prices"]["currency"]
#     }
# )


# print(products)

# TODO: Exercise 6: Create 'get_products' function
#  1. Create a new function called 'get_products'
#  2. 'get_products' function takes 1 argument 'res_data'
#  3. The goal of the function is to return a list of 5 products
#  4. Each product should be appended to the 'products' list
#    as a Dict with with product 'title', 'image', 'full_link',
#    'current_price', 'currency'
#  5. Use 'for loop' to with 'break' statement to end the 'for loop' once
#  you have collected 5 products
#  6. Use if statement to only add products with current_price higher than
#  -1.0 (float)
#  7. The function should return a list of products (add a return type
#  to the function)


# def get_products(res_data: Dict) -> List:
#     products: List = []
#
#     for product in res_data["results"]:
#         if len(products) == 5:
#             break
#         else:
#             if product["prices"]["current_price"] == -1.0:
#                 continue
#             else:
#                 products.append(
#                     {
#                         "title": product["title"],
#                         "image": product["image"],
#                         "full_link": product["full_link"],
#                         "current_price": product["prices"]["current_price"],
#                         "currency": product["prices"]["currency"]
#                     }
#                 )
#
#     return products

# TODO: Exercise 7: Create 'Products' class
#  1. Move 'get_products()' function to the 'Products' class
#  2. Rename 'get_products()' function to just 'get()' method
#  3. Create __init__ method with two arguments:
#    'res_data' and 'amount'
#  4. Create two variables in __init__ method:
#    'self.data' (for 'res_data') and 'self.amount' for 'amount'
#  5. Use 'self.data' and  'self.amount' in 'get()' method

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


products = Products(res_data=res.json(), amount=5).get()

# print(products)
# print(len(products))

# TODO: Exercise 8: Write a list of products text to a file
#  1. Learn how to create text files with Python using the simple example below
#  2. Adjust simple example code to create your own products.txt file
#  3. Make sure products.txt file content corresponds to the example below

products_text: str = ""

for index, product in enumerate(products):
    products_text += f"Product #{index}:\n"
    products_text += f"    {product['title']}\n"
    products_text += f"    Price: {product['current_price']}\n"
    products_text += f"    Link: {product['full_link']}\n\n\n"

with open("products.txt", "w") as f:
    f.write(products_text)

with open("products.txt", "r") as f:
    products_file = f.read()
    print(products_file)
