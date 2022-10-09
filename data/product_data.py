from dataclasses import dataclass
from datetime import datetime
import random
import string


@dataclass
class Product:
    product_name: str = None
    description: str = None
    meta_tag_title: str = None
    meta_tag_description: str = None
    meta_tag_keywords: str = None
    product_tags: str = None
    model: str = None
    sku: str = None
    ean: str = None
    jan: str = None
    isbn: str = None
    mpn: str = None
    location: str = None
    price: int = None
    tax_class: str = None
    quantity: str = None
    minimum_quantity: str = None
    subtract_stock: str = None
    out_of_stock_status: str = None
    requires_shipping: bool = None
    date_available: datetime = None
    dimensions: list = None
    length_class: float = None
    weight: float = None
    weight_class: float = None
    status: str = None
    sort_order: int = None


class ProductTestData:

    def generate_random_product(self):
        p = Product()
        p.product_name = "1" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
        p.description = ''.join(random.choices(string.ascii_lowercase + string.digits, k=100))
        p.meta_tag_title = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
        p.model = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        p.price = random.randint(1, 100000)

        return p


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    e_mail: str = None
    phone: str = None
    password: str = None


class UserTestData:

    def generate_random_user(self):
        user = User()
        user.first_name = ''.join(random.choices(string.ascii_lowercase, k=10)).title()
        user.last_name = ''.join(random.choices(string.ascii_lowercase, k=15)).title()
        user.e_mail = ''.join(random.choices(string.ascii_letters + string.digits, k=20)) + \
                      "@" + \
                      random.choice(["mail", "google", "yandex"]) + \
                      "." + \
                      random.choice(["com", "ru"])
        user.phone = "+7" + ''.join(random.choices(string.digits, k=10))
        user.password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        return user

