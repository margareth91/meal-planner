from django.contrib.auth import get_user_model
from django.test import TestCase

from planner.models import Meal

User = get_user_model()


class MealModelTest(TestCase):
    MEAL_NAME = "Meal"
    MEAL_DESCRIPTION = "Meal description"

    def setUp(self):
        self.author = User.objects.create()
        Meal.objects.create(
            author=self.author, name=self.MEAL_NAME, description=self.MEAL_DESCRIPTION
        )
        self.meal = Meal.objects.get(id=1)

    def test_meal_author(self):
        self.assertTrue(self.meal.author, self.author)

    def test_meal_name(self):
        self.assertEqual(self.meal.name, self.MEAL_NAME)

    def test_meal_description(self):
        self.assertEqual(self.meal.description, self.MEAL_DESCRIPTION)

    def test_str(self):
        self.assertEqual(self.meal.__str__(), self.meal.name)
