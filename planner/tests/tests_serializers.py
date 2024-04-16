from django.contrib.auth.models import User
from django.test import TestCase

from planner.models import Meal
from planner.serializers import MealSerializer


class MealSerializerTest(TestCase):
    MEAL_NAME = "Meal"
    MEAL_DESCRIPTION = "Meal description"

    def setUp(self):
        self.author = User.objects.create()
        self.meal = Meal.objects.create(
            author=self.author, name=self.MEAL_NAME, description=self.MEAL_DESCRIPTION
        )
        self.meal_serializer = MealSerializer(instance=self.meal)
        self.meal_serializer_data = self.meal_serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            self.meal_serializer_data.keys(), {"id", "author", "name", "description"}
        )

    def test_id_field(self):
        self.assertEqual(self.meal_serializer_data["id"], self.meal.id)

    def test_author_content(self):
        self.assertEqual(self.meal_serializer_data["author"], self.meal.author.id)

    def test_name_content(self):
        self.assertEqual(self.meal_serializer_data["name"], self.MEAL_NAME)

    def test_description_content(self):
        self.assertEqual(
            self.meal_serializer_data["description"], self.MEAL_DESCRIPTION
        )
