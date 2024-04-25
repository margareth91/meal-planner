from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class CustomUserManagerTest(TestCase):
    EMAIL = "user@app.com"
    PASSWORD = "password"

    def test_create_superuser_successfully(self):
        superuser = User.objects.create_superuser(
            email=self.EMAIL, password=self.PASSWORD, is_staff=True, is_superuser=True
        )
        self.assertTrue(isinstance(superuser, User))

    def test_create_superuser_failure_if_isstaff_false(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=self.EMAIL,
                password=self.PASSWORD,
                is_staff=False,
                is_superuser=True,
            )

    def test_create_superuser_failure_if_issuperuser_false(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=self.EMAIL,
                password=self.PASSWORD,
                is_staff=True,
                is_superuser=False,
            )
