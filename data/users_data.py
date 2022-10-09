from dataclasses import dataclass
import random
import string


@dataclass
class ModelUser:
    first_name: str = None
    last_name: str = None
    e_mail: str = None
    phone: str = None
    password: str = None


class UserTestData:

    def generate_random_user(self):
        user = ModelUser()
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
