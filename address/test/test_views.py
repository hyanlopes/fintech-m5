from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User


class AddressViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = {
            "username": "mallorga",
            "email": "mallorga@gmail.com",
            "password": "1234",
            "birth_date": "1994-09-04",
            "first_name": "rafhael",
            "last_name": "mallorga",
            "cpf": "109.529.500-49",
        }
        cls.address = {
            "zip_code": "1234567",
            "address": "Rua não sei oq",
            "number": 13,
            "complement": "Algum complemento",
            "district": "Esse mesmo",
            "city": "Aquela cidade",
            "country": "Br",
            "state": "RJ",
        }
        cls.user_login = User.objects.create_user(**cls.user)
        cls.user_login_token = Token.objects.get_or_create(user=cls.user_login)

    def test_create_address_success(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_login_token[0]}")
        response = self.client.post("/api/address/", self.address, format="json")

        self.assertEqual(201, response.status_code)

    def test_create_address_with_no_user(self):
        response = self.client.post("/api/address/", self.address, format="json")

        self.assertEqual(401, response.status_code)
        self.assertIn("detail", response.data)
