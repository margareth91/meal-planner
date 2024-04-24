from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class UserSignUpViewTest(APITestCase):
    EMAIL = "user@app.com"
    USERNAME = "User"
    PASSWORD = "password"

    def setUp(self):
        self.user = User.objects.create(
            email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD
        )

    def test_new_user_created_successfully(self):
        new_user = {
            "email": "email@email.com",
            "username": "username",
            "password": "password#123",
        }
        self.client.login(email=self.EMAIL, password=self.PASSWORD)
        response = self.client.post(reverse("signup"), new_user)
        self.assertEqual(response.status_code, 201)


class UserLoginViewTest(APITestCase):
    EMAIL = "user@app.com"
    USERNAME = "User"
    PASSWORD = "password"

    def setUp(self):
        self.user = User.objects.create(
            email=self.EMAIL, username=self.USERNAME, password=self.PASSWORD
        )

    def test_login_successfully(self):
        request_text = {"email": self.EMAIL, "password": self.PASSWORD}
        response = self.client.post(reverse("login"), request_text)
        self.assertEqual(response.status_code, 200)
