from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User


class UserViewTest(APITestCase):
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

        cls.user_2 = {
            "username": "tárcila",
            "email": "tárcila@gmail.com",
            "password": "1234",
            "birth_date": "1985-10-31",
            "first_name": "tárcila",
            "last_name": "garcia",
            "cpf": "402.780.350-78",
        }
        cls.user_3 = {
            "username": "hyan",
            "email": "hyan@gmail.com",
            "password": "1234",
            "birth_date": "1985-10-31",
            "first_name": "hyan",
            "last_name": "lopes",
            "cpf": "402.780.350-78",
        }
        cls.user_login = User.objects.create_user(**cls.user_2)
        cls.user_login_token = Token.objects.get_or_create(user=cls.user_login)

        cls.admin_login = User.objects.create_superuser(**cls.user_3)
        cls.admin_login_token = Token.objects.get_or_create(user=cls.admin_login)

        cls.user_login_account = {
            "username": "tárcila",
            "password": "1234",
        }

    def test_can_create_user(self):
        response = self.client.post("/api/users/register/", self.user, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["username"], self.user["username"])
        self.assertEqual(response.data["email"], self.user["email"])
        self.assertEqual(response.data["birth_date"], self.user["birth_date"])
        self.assertEqual(response.data["first_name"], self.user["first_name"])
        self.assertEqual(response.data["last_name"], self.user["last_name"])
        self.assertEqual(response.data["cpf"], self.user["cpf"])

    def test_login(self):
        response = self.client.post(
            "/api/login/", self.user_login_account, format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["token"])

    def test_list_all_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.admin_login_token[0]}")
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, 200)

    def test_list_all_users_unsuccessfully(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_login_token[0]}")
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, 403)

    def test_list_especific_user_owning(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_login_token[0]}")
        response = self.client.get(f"/api/users/{self.user_login.id}/")
        self.assertEqual(200, response.status_code)

    def test_list_especific_user_not_being_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_login_token[0]}")
        response = self.client.get(f"/api/users/{self.admin_login.id}/")
        self.assertEqual(403, response.status_code)
