from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):
    EMAIL = "user@app.com"
    USERNAME = "User"
    PASSWORD = "password"

    def setUp(self):
        self.user = User.objects.create_user(
            email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD
        )

    def test_user_created(self):
        user = User.objects.filter(username=self.USERNAME)
        self.assertTrue(user.exists())

    def test_str(self):
        self.assertEqual(self.user.__str__(), self.USERNAME)
