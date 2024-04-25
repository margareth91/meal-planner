from django.db.utils import IntegrityError
from django.test import TestCase

from accounts.models import User
from accounts.serializers import UserSignUpSerializer


class UserSignUpSerializerTest(TestCase):
    EMAIL = "user@app.com"
    USERNAME = "User"
    PASSWORD = "password"

    def setUp(self):
        self.user = User.objects.create_user(
            email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD
        )
        self.user_serializer = UserSignUpSerializer(instance=self.user)
        self.user_serializer_data = self.user_serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(self.user_serializer_data.keys(), {"email", "username"})

    def test_create_user_with_same_email_failure(self):
        with self.assertRaises(IntegrityError):
            self.user2 = User.objects.create_user(
                email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD
            )
