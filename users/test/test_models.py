from django.test import TestCase

from users.models import User

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = {
            'username': 'lucira',
            'email': 'lucira@gmail.com',
            'birth_date': '2000-08-28', 
            'first_name': 'lucira',
            'last_name' : 'silva' ,
            'cpf': '693.489.970-92'
        }

        cls.user_instance = User.objects.create_user(**cls.user)

    def test_user_atributes(self):
        self.assertEqual(self.user_instance.username, self.user['username'])
        self.assertEqual(self.user_instance.email, self.user['email'])
        self.assertEqual(self.user_instance.birth_date, self.user['birth_date'])
        self.assertEqual(self.user_instance.first_name, self.user['first_name'])
        self.assertEqual(self.user_instance.last_name, self.user['last_name'])
        self.assertEqual(self.user_instance.cpf, self.user['cpf'])

    
