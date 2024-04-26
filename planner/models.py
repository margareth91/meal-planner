from django.conf import settings
from django.db import models

DAY_OF_THE_WEEK = [
    ("1", "Monday"),
    ("2", "Tuesday"),
    ("3", "Wednesday"),
    ("4", "Thursday"),
    ("5", "Friday"),
    ("6", "Saturday"),
    ("7", "Sunday"),
]


class Meal(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    weekday = models.CharField(choices=DAY_OF_THE_WEEK, max_length=10)

    def __str__(self):
        return self.name
