import random
import string
from dataclasses import dataclass


@dataclass()
class UserGenerator:
    first_name: str
    last_name: str
    password: str
    email: str

    @staticmethod
    def generate_email_address():
        return "test_mail" + "".join(random.choices(string.digits, k=8)) + "@gmail.com"

    @staticmethod
    def geneate_password():
        return "".join(random.choices(string.digits, k=5)) + "".join(random.choices(string.ascii_letters, k=5))

    def get_user(key):
        users = {
            "Common user": UserGenerator(first_name='Meant', last_name='Bot',
                                         password=UserGenerator.geneate_password(), email=''),
            "Registered user": UserGenerator(first_name='Meant', last_name='Bot',
                                             password='1234qweR', email='meant4_bot@gmail.com')
        }
        return users[key]
