from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.UserSignUpView.as_view(), name="signup"),
]
